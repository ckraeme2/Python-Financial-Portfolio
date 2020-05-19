import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from get_data import get_data

data = get_data()
style.use('ggplot')
column = input("Enter data to be graphed (if all, enter all): ")
if column == 'all':
    data.plot()
else:
    data[column].plot()

plt.show()
