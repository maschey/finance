#!/usr/bin/python3.8

import plotly.graph_objects as go
import requests
import pandas as pd

# get bitcoin Data in 15min steps
btc = requests.get(
    'https://financialmodelingprep.com/api/v3/historical-chart/15min/BTCUSD?apikey=')
df = pd.DataFrame.from_dict(btc.json())
dfs = df[:10]

eurUSD = requests.get(
    'https://financialmodelingprep.com/api/v3/quote/EURUSD?apikey=')
eurUSDResponse = eurUSD.json()

fig = go.Figure(data=[go.Candlestick(x=dfs['date'],
                                     open=dfs['open'] / eurUSDResponse[0]['price'],
                                     high=dfs['high'] / eurUSDResponse[0]['price'],
                                     low=dfs['low'] / eurUSDResponse[0]['price'],
                                     close=dfs['close'] / eurUSDResponse[0]['price']
                                     )])

fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), xaxis_rangeslider_visible=False, height=300, width=300)
fig.write_image("gespeichertesdiagramm.png")
