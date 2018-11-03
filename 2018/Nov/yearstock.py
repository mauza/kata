import os
import pandas as pd
import json
import datetime as dt
import pandas_datareader.data as web 

date = '2018-11-02'

def stdev(ticker):
    end = dt.date.today()
    start = dt.date.today()-dt.timedelta(days=365)
    df = web.DataReader(ticker, 'yahoo', start, end)
    p = pd.concat([df['High'], df['Low'], df['Open'], df['Close']])
    p = p.sort_index()
    print(p)
    return [p.std(), p[-22*4:].std(), p[-5*4:].std()]

print(stdev("ENR"))