# The user has now entered the data and it is now saved to a CSV
# The next step is to plot this data to a graph that updates itself each time the user logs/inputs new data/ hours learning
# The graph should plot the goal hours and the time actually spent learning to code. 

from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
from matplotlib import style 

style.use('ggplot')


df = pd.read_csv('total_tracked_coding_hours.csv')



# plt.plot(x,y, label='First line')
# plt.plot(x2,y2, label='Second line')
# plt.xlabel('Plot Number')
# plt.ylabel('Important var')
# plt.title('Interesting Graph\n Check it out')
# plt.legend()
# plt.show()