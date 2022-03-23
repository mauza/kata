from datetime import datetime
from dotenv import load_dotenv
import os, requests, sys, json

load_dotenv()

SYMBOL = "ETH"
API_KEY = os.environ["CRYPTOCOMPARE_API_KEY"]


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

def main():
    filename = f'data/{SYMBOL}_2021.json'
    data = get_data(datetime.timestamp(datetime(2021, 1, 1)), datetime.timestamp(datetime(2021, 12, 31)))
    for hour_data in data:
        d = json.dumps(hour_data)
        with open(filename, 'a') as f:
            f.write(d + "\n")
 

if __name__ == "__main__":
    main()