from dateutil import parser
from datetime import datetime
from dotenv import load_dotenv
import os, requests, sys, json
import pandas

load_dotenv()

API_KEY = os.environ["CRYPTOCOMPARE_API_KEY"]
BTC = pandas.read_json('data/BTC_2021.json', lines=True)
ETH = pandas.read_json('data/ETH_2021.json', lines=True)
prices = {"BTC": BTC, "ETH": ETH}

def get_data(start_ts, end_ts):
    data = []
    ts = end_ts
    while ts > start_ts:
        url = f"https://min-api.cryptocompare.com/data/v2/histohour?fsym={SYMBOL}&tsym=USD&limit=2000&toTs={ts}&api_key={API_KEY}"
        response = requests.get(url).json()
        if response["Type"] != 100:
            raise(Exception("Bad Response"))
        ts = response["Data"]["TimeFrom"]
        data += response["Data"]["Data"]
    return data

def get_historical(year, symbol):
    filename = f'data/{symbol}_{year}.json'
    data = get_data(datetime.timestamp(datetime(year, 1, 1)), datetime.timestamp(datetime(year, 12, 31)))
    for hour_data in data:
        d = json.dumps(hour_data)
        with open(filename, 'a') as f:
            f.write(d + "\n")

def find_neighbours(value, df, colname):
    exactmatch = df[df[colname] == value]
    if not exactmatch.empty:
        return exactmatch.index
    else:
        lowerneighbour_ind = df[df[colname] < value][colname].idxmax()
        upperneighbour_ind = df[df[colname] > value][colname].idxmin()
        return [lowerneighbour_ind, upperneighbour_ind]  

def get_price(t, symbol):
    ts = datetime.timestamp(t)
    ns = find_neighbours(ts, prices[symbol], "time")
    result = prices[symbol].at[ns[0], "low"]
    return result
 
def main():
    account = pandas.read_csv('data/account.csv')
    account["Current_USD_Conversion"] = account["time"].map(lambda t: get_price(parser.parse(t), "BTC"))
    account.to_csv('data/test.csv', index=False)

if __name__ == "__main__":
    main()