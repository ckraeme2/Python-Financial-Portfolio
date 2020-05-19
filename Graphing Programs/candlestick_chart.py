import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import mplfinance as mpf
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web
from get_data import get_data


data = get_data()
data.index = pd.to_datetime(data.index)

mpf.plot(data[-50:], type='candlestick', show_nontrading= True)
