# importing our credentials (Check documentation).
import config
import pandas as pd

# Binance API.
from binance.client import Client

# Loading keys from config file and setting up connection.
client = Client(config.API_KEY, config.API_SECRET)

pd.set_option('float_format', '{:f}'.format)

print(client.ping())    # Check if we are in.

# Our asset is Ethereum.
PAIR = 'ETHUSDT'

# 3 minute data.
INTERVAL = '3m'

# For the last 1 day.
LOOKBACK = '1d'

# Function which collects our data and transforms our dictionary to a more readable format.
def getdaydata(symbol, interval, lookback):
    frame = pd.DataFrame(client.get_historical_klines(
        symbol, interval, lookback))
    # From documentation, we decide to keep those columns which are:
    frame = frame.iloc[:, :6]
    frame.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    frame = frame.set_index('Date')
    # Transforming into datetime format.
    frame.index = pd.to_datetime(frame.index, unit='ms')
    frame = frame.astype(float)  # The rest columns contain float values.
    return frame


# get our df with time interval of 3 minutes and lookback 1 day ago.
df = getdaydata(PAIR, INTERVAL, LOOKBACK)

print(df)

# Save a csv file in the same directory of the script.
df.to_csv('./scrapped_data.csv', index=True, header=True)
