import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import matplotlib.ticker as mticker
import pandas as pd

def get_price_ts(in_ticker, api_key, start_date):
    url = "https://rest.coinapi.io/v1/ohlcv/{}/history?period_id=1DAY&time_start=2017-01-01T00:00:00&limit=3000".format(in_ticker)
    headers = {'X-CoinAPI-Key': api_key}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        price_hist = response.json()
        #dates = [datetime.fromisoformat(item['time_period_start'][:-1]).date() for item in price_hist]
        dates = [item['time_period_start'] for item in price_hist]
        closes = [item['price_close'] for item in price_hist]
        df = pd.DataFrame()
        df['date'] = dates;
        df['price'] = closes;
        df.set_index('date', inplace=True)
        #start_date_obj = datetime.strptime(start_date, '%Y-%m-%d').date()
        #df = df[df.index >= start_date_obj]
        return df

    else:
        print("Failed to fetch data: Status code", response.status_code)
        print("Response:", response.text)
        return None
