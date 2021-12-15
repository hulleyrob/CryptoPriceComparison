#!/usr/bin/env python3

from datetime import datetime, timedelta
from sklearn.preprocessing import MinMaxScaler,MaxAbsScaler
import pandas as pd
import pandas_datareader as pdr
import plotly.graph_objects as go

CRYPTOS = ['BTC', 'ETH', 'ADA', 'ANKR', 'DOT1','SOL1','HEX','BNB','DOGE','LUNA1','SHIB','XLM','LINK']
# CRYPTOS = ['BTC', 'ETH', 'ADA']
CURRENCY = 'USD'

def getData(cryptocurrency):
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    last_year_date = (now - timedelta(days=100)).strftime("%Y-%m-%d")
    start = pd.to_datetime(last_year_date)
    end = pd.to_datetime(current_date)
    data = pdr.get_data_yahoo(f'{cryptocurrency}-{CURRENCY}', start, end)
    print(f"{data=}")
    data = pd.DataFrame(MaxAbsScaler().fit_transform(data), columns=data.columns)
    return data
crypto_data = {crypto:getData(crypto) for crypto in CRYPTOS}
fig = go.Figure()
for idx, name in enumerate(crypto_data):
    fig = fig.add_trace(
        go.Scatter(
            x = crypto_data[name].index,
            y = crypto_data[name].Close * 100,
            name = name,
        ))
fig.update_layout(
    title = 'The Correlation between Different Cryptocurrencies',
    xaxis_title = 'Days',
    yaxis_title = f'Closing price per day as perentage of Max price (%)',
    legend_title = 'Cryptocurrencies')
fig.update_yaxes(type='linear', tickprefix='',ticksuffix='%')
fig.show()
