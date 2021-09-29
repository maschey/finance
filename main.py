import matplotlib.pyplot as plt
import requests
import os
from datetime import datetime
import arrow

apikey = os.environ['apikey']
# get bitcoin Data in 15min steps
btc = requests.get(
    'https://financialmodelingprep.com/api/v3/historical-chart/15min/BTCUSD?apikey=' + apikey)
btcResponse = btc.json()

# get live EUR/USD ratio
eurUSD = requests.get(
    'https://financialmodelingprep.com/api/v3/quote/EURUSD?apikey=' + apikey)
eurUSDResponse = eurUSD.json()

# time beam (Does Zeitstrahl mean time beam in english? idk)
xValues = ['-2,25',
           '-2',
           '-1,75',
           '-1,5',
           '-1,25',
           '-1',
           '-0,75',
           '-0,5',
           '-0,25',
           'Jetzt'
           ]

# conversion of USD in EUR
yValues = []

i = 0
while i < 10:
    yValues.insert(0, btcResponse[i]['high'] / eurUSDResponse[0]['price'])
    i = i + 1

# convert timestamp string to datetime and convert datetime-timestamp to localtime in BERLIN/AMSTERDAM
# (i hope -0500 is right but honestly i don't know exactly)
datetimeObj = datetime.strptime(btcResponse[0]['date'] + ' -0500', '%Y-%m-%d %H:%M:%S %z')
time_of_update = arrow.get(datetimeObj).to('Europe/Berlin').format().split(' ')[1].split('+')[0]

# set sizes, because motherfucking teamspeak can handle only 300x300px, later on dpi is set to 70, for geniuses 70*5=300
figure = plt.gcf()
figure.set_size_inches(5, 5)

# set labels to markers
for x, y in zip(xValues, yValues):
    label = '{:.2f}'.format(y / 1000).replace('.', ',') + 'k'

    plt.annotate(label, (x, y), textcoords='offset points', xytext=(0, 10))

# render this shit and draw a png
plt.plot(xValues, yValues, markersize=1)
plt.xlabel('Zeitachse in Stunden' + ' (Stand: ' + time_of_update + ' Uhr)')
plt.ylabel('BTC Wert in €EUR')
plt.tight_layout()
plt.scatter(xValues, yValues, color='red')
plt.savefig('gespeichertesdiagramm.png', dpi=70)