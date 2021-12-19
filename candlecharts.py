#!/usr/bin/python3.8
import os
import plotly.graph_objects as go
import requests
import pandas as pd

apikey = os.environ['apikey']
urlUSD = 'https://financialmodelingprep.com/api/v3/quote/EURUSD?apikey=' + apikey
urlBTC = 'https://financialmodelingprep.com/api/v3/historical-chart/15min/BTCUSD?apikey=' + apikey

eurUSD = requests.get(urlUSD)
eurUSDResponse = eurUSD.json()

btc = requests.get(urlBTC)
df = pd.DataFrame.from_dict(btc.json())

dfs = df.iloc[0:10]
dfs['date'] = pd.to_datetime(dfs['date'])
dfs.date = dfs.date.dt.tz_localize('EST').dt.tz_convert('Europe/Berlin')
dfs.sort_values(by=['date'], inplace=True, ascending=True)

fig = go.Figure(data=[go.Candlestick(x=dfs['date'].apply(lambda t: t.strftime('%H:%M')),
                                     open=dfs['open'] / eurUSDResponse[0]['price'],
                                     high=dfs['high'] / eurUSDResponse[0]['price'],
                                     low=dfs['low'] / eurUSDResponse[0]['price'],
                                     close=dfs['close'] / eurUSDResponse[0]['price']
                                     )])

fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), xaxis_rangeslider_visible=False, height=300, width=300)
fig.write_image("gespeichertesdiagramm.png")
