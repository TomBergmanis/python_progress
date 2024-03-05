# The user has now entered the data and it is now saved to a CSV
# The next step is to plot this data to a graph that updates itself each time the user logs/inputs new data/ hours learning
# The graph should plot the goal hours and the time actually spent learning to code. 

from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
from matplotlib import style 

style.use('fivethirtyeight')

df = pd.read_csv('total_tracked_coding_hours.csv', parse_dates=['Date'], dayfirst=True)

df.set_index("Date", inplace=True)

plt.plot(df.index, df['Total Hours'])
plt.xticks(df.index, rotation=45)
plt.xlabel('Date')
plt.ylabel('Total Hours')
plt.title('Total Tracker Coding Hours Over Time')

plt.subplots_adjust(left=0.083, bottom=0.212,right=0.94, top=0.936, wspace=0.2, hspace=0)

plt.show()
