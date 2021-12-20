#!/usr/bin/python3.8
import os
import plotly.graph_objects as go
import requests
import pandas as pd

apikey = os.environ['apikey']
eur_usd_ratio_request = 'https://financialmodelingprep.com/api/v3/quote/EURUSD?apikey=' + apikey
btc_request = 'https://financialmodelingprep.com/api/v3/historical-chart/15min/BTCUSD?apikey=' + apikey

euro_usd_ratio_response = requests.get(eur_usd_ratio_request)
eur_usd_ratio = euro_usd_ratio_response.json()

btc = requests.get(btc_request)
btc_df = pd.DataFrame.from_dict(btc.json())

btc_df = btc_df.iloc[0:10]
btc_df['date'] = pd.to_datetime(btc_df['date'])
btc_df.date = btc_df.date.dt.tz_localize('EST').dt.tz_convert('Europe/Berlin')
btc_df.sort_values(by=['date'], inplace=True, ascending=True)

fig = go.Figure(data=[go.Candlestick(x=btc_df['date'].apply(lambda t: t.strftime('%H:%M')),
                                     open=btc_df['open'] / eur_usd_ratio[0]['price'],
                                     high=btc_df['high'] / eur_usd_ratio[0]['price'],
                                     low=btc_df['low'] / eur_usd_ratio[0]['price'],
                                     close=btc_df['close'] / eur_usd_ratio[0]['price']
                                     )])

fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), xaxis_rangeslider_visible=False, height=300, width=300)
fig.write_image("gespeichertesdiagramm.png")
