import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

def get_data():

    startString = input("Enter the first date from which to get data in format (year month day): ")
    endString = input("Enter the last date from which to get data in format (year month day): ")

    startTerms = startString.split()
    endTerms = endString.split()

    start = dt.datetime(int(startTerms[0]), int(startTerms[1]), int(startTerms[2]))
    end = dt.datetime(int(endTerms[0]), int(endTerms[1]), int(endTerms[2]))

    ticker = input("Enter the ticker of the stock of interest: ")
    api = input("Enter the name of the desired api: ")
    df = web.DataReader(ticker, api, start, end)

    maSpan = input("Enter # of days for moving average calculation: ")

    df[maSpan + 'ma'] = df['Adj Close'].rolling(window=int(maSpan), min_periods=0).mean()

    df.to_csv(ticker + '.csv')

    data = pd.read_csv((ticker + '.csv'), index_col = 'Date')

    return data
