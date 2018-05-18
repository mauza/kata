from yahoo_finance import Share
import csv

google = Share('GOOGL')

google_year = google.get_historical('2016-1-19', '2017-1-13')

start_money = 10000

Low = -0.033
High = 0.021

stock, extra = divmod(start_money, float(google_year[-1]['Close']))
no_trading = stock*float(google_year[0]['Close']) + extrabring
print(no_trading)

