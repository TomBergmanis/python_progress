import datetime
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data from the CSV file (assuming it has 'Date' and 'Total Hours' columns)
df = pd.read_csv('total_tracked_coding_hours.csv', parse_dates=['Date'], dayfirst=True)

# Create a new DataFrame to track weekly contributions
weekly_contributions = df.resample('W-Mon', label='left', closed='right')['Total Hours'].sum()

# Create a matrix to represent the heatmap
heatmap_data = weekly_contributions.values.reshape(-1, 7)

# Get the corresponding dates for the x-axis
heatmap_dates = weekly_contributions.index.strftime('%Y-%m-%d').tolist()

# Set up the Seaborn heatmap
sns.set(style="white")
plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, cmap="YlGnBu", annot=True, fmt=".1f", linewidths=.5, xticklabels=7, yticklabels=False)

plt.title('Weekly Coding Contributions')
plt.xlabel('Days of the Week')
plt.ylabel('Weeks')
plt.xticks(np.arange(7) + 0.5, ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])

plt.show()
