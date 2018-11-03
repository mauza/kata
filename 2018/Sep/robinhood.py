import requests
import logging
import warnings
from six.moves.urllib.request import getproxies

import exceptions as RH_exception
from config import USER, PASS

url = "https://api.robinhood.com/options/positions/"

class Robinhood:
    """wrapper class for fetching/parsing Robinhood endpoints"""
    endpoints = {
        "login": "https://api.robinhood.com/oauth2/token/",
        "logout": "https://api.robinhood.com/api-token-logout/",
        "investment_profile": "https://api.robinhood.com/user/investment_profile/",
        "accounts": "https://api.robinhood.com/accounts/",
        "ach_iav_auth": "https://api.robinhood.com/ach/iav/auth/",
        "ach_relationships": "https://api.robinhood.com/ach/relationships/",
        "ach_transfers": "https://api.robinhood.com/ach/transfers/",
        "applications": "https://api.robinhood.com/applications/",
        "dividends": "https://api.robinhood.com/dividends/",
        "edocuments": "https://api.robinhood.com/documents/",
        "instruments": "https://api.robinhood.com/instruments/",
        "instruments_popularity": "https://api.robinhood.com/instruments/popularity/",
        "margin_upgrades": "https://api.robinhood.com/margin/upgrades/",
        "markets": "https://api.robinhood.com/markets/",
        "notifications": "https://api.robinhood.com/notifications/",
        "options_positions": "https://api.robinhood.com/options/positions/",
        "orders": "https://api.robinhood.com/orders/",
        "password_reset": "https://api.robinhood.com/password_reset/request/",
        "portfolios": "https://api.robinhood.com/portfolios/",
        "positions": "https://api.robinhood.com/positions/",
        "quotes": "https://api.robinhood.com/quotes/",
        "historicals": "https://api.robinhood.com/quotes/historicals/",
        "document_requests": "https://api.robinhood.com/upload/document_requests/",
        "user": "https://api.robinhood.com/user/",
        "watchlists": "https://api.robinhood.com/watchlists/",
        "news": "https://api.robinhood.com/midlands/news/",
        "ratings": "https://api.robinhood.com/midlands/ratings/",
        "fundamentals": "https://api.robinhood.com/fundamentals/",
        "options": "https://api.robinhood.com/options/",
        "marketdata": "https://api.robinhood.com/marketdata/"
    }

    session = None

    username = None

    password = None

    headers = None

    auth_token = None

    def __init__(self):
        self.session = requests.session()
        self.session.proxies = getproxies()
        self.headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en;q=1, fr;q=0.9, de;q=0.8, ja;q=0.7, nl;q=0.6, it;q=0.5",
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            "X-Robinhood-API-Version": "1.0.0",
            "Connection": "keep-alive",
            "User-Agent": "Robinhood/823 (iPhone; iOS 7.1.2; Scale/2.00)",
            "Origin": "https://robinhood.com"
        }
        self.session.headers = self.headers
        self.login(USER, PASS)

    def login(
            self,
            username,
            password,
            mfa_code=None
        ):
        """save and test login info for Robinhood accounts

        Args:
            username (str): username
            password (str): password

        Returns:
            (bool): received valid auth token

        """
        self.username = username
        self.password = password
        payload = {
            'password': self.password,
            'username': self.username,
            'scope': 'internal',
            'grant_type': 'password',
            'client_id': 'c82SH0WZOsabOXGP2sxqcj34FxkvfnWRZBKlBjFS',
            'expires_in': 86400
        }

        if mfa_code:
            payload['mfa_code'] = mfa_code

        try:
            res = self.session.post(
                self.endpoints['login'],
                data=payload
            )
            res.raise_for_status()
            data = res.json()
        except requests.exceptions.HTTPError:

            raise RH_exception.LoginFailed()

        if 'mfa_required' in data.keys():           #pragma: no cover
            raise RH_exception.TwoFactorRequired()  #requires a second call to enable 2FA

        if 'access_token' in data.keys():
            self.auth_token = data['access_token']
            self.headers['Authorization'] = 'Bearer ' + self.auth_token
            return True

        return False
    
    def logout(self):
        """logout from Robinhood

        Returns:
            (:obj:`requests.request`) result from logout endpoint

        """
        try:
            req = self.session.post(self.endpoints['logout'])
            req.raise_for_status()
        except requests.exceptions.HTTPError as err_msg:
            warnings.warn('Failed to log out ' + repr(err_msg))

        self.headers['Authorization'] = None
        self.auth_token = None

        return req

    def quote_data(self, stock=''):
        """fetch stock quote
        Args:
            stock (str): stock ticker, prompt if blank
        Returns:
            (:obj:`dict`): JSON contents from `quotes` endpoint
        """
        url = None
        if stock.find(',') == -1:
            url = str(self.endpoints['quotes']) + str(stock.upper()) + "/"
        else:
            url = str(self.endpoints['quotes']) + "?symbols=" + str(stock.upper())
        #Check for validity of symbol
        try:
            req = requests.get(url)
            req.raise_for_status()
            data = req.json()
        except requests.exceptions.HTTPError:
            raise NameError('Invalid Symbol: ' + stock) #TODO: custom exception

        return data

    def get_quote(self, stock=''):
        """wrapper for quote_data"""
        data = self.quote_data(stock)
        return data["symbol"]

    ##############################
    # GET OPTIONS POSITIONS
    ##############################

    def options_owned(self):
        options = self.session.get(self.endpoints['options'] + "positions/?nonzero=true").json()
        options = options['results']
        return options

    def get_option_marketdata(self, instrument):
        info = self.session.get(self.endpoints['marketdata'] + "options/?instruments=" + instrument).json()
        return info['results'][0]

    def get_option_chainid(self, symbol):
        stock_info = self.session.get(self.endpoints['instruments'] + "?symbol=" + symbol).json()
        stock_id = stock_info['results'][0]['id']
        params = {}
        params['equity_instrument_ids'] = stock_id
        chains = self.session.get(self.endpoints['options'] + "chains/", params = params).json()
        chains = chains['results']
        chain_id = None

        for chain in chains:
            if chain['can_open_position'] == True:
                chain_id = chain['id']

        return chain_id

    def get_option_quote(self, arg_dict):
        chain_id = self.get_option_chainid(arg_dict.pop('symbol', None))
        arg_dict['chain_id'] = chain_id
        option_info = self.session.get(self.endpoints['options'] + "instruments/", params = arg_dict).json()
        option_info = option_info['results']
        exp_price_list = []

        for op in option_info:
            mrkt_data = self.get_option_marketdata(op['url'])
            op_price = mrkt_data['adjusted_mark_price']
            exp = op['expiration_date']
            exp_price_list.append((exp, op_price))

        exp_price_list.sort()

        return exp_price_list
