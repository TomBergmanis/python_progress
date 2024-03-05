import csv
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
from matplotlib import style 

style.use('ggplot')


# Monthly Tracker done by week 

months = ['January','February','March','April','May','June','July','August','September','October','November','Decemeber']

# Takes the total number of hours spent learning to code each day of the week.
# Ask the user to input the number of hours spent learning to code for each day of the week.
# Save that number for each day in a csv. 
# Adds them up for a total for each week
# Save that in a new csv
# Create a bar chart that shows the total hours for each week and display for the whole year. 
# break it down to monthly e.g. January would have 4 mini bars, February would have 4 mini bars and so on.
# The graph should show an overview of time spent each week learning to code and can be visualised by the graph.
""" Create a constant to compare to. 
    If the goal was to spend 35 hours a week coding then there should be a line going 
    straight across the graph and the user can see if they meet that target or not 
    based on whether their bars hit the line or exceed it
"""

# Once completed add a trend line to show where the most time was spent 

# This section gets the user to input their time spent learning to code during the week and then saves it to a CSV file for later
# Daily Data 
def main():
    # Initialize variables
    coding_data = []
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    global goal_setting
    goal_setting = float(input("What is your goal for how many hours you plan to spend learning to code this week: "))

    # Input coding hours for each day
    for day in days_of_week:
        while True:
            try:
                hours = float(input(f"For {day}, how many hours did you spend learning to code? "))
                if 0 <= hours <= 24:
                    break
                else:
                    print("Please enter a valid number between 0 and 24.")
            except ValueError:
                print("Please enter a valid number.")

        # Calculate the date for the specific day entered
        current_date = datetime.now()
        day_of_week = days_of_week.index(day)
        delta_days = (current_date.weekday() - day_of_week) % 7
        specific_date = current_date - timedelta(days=delta_days)

        # Check if the calculated date is in the future
        if specific_date > current_date:
            print(f"Please enter a valid time for {day}. The date for {day} has not occurred yet.")
            continue

        coding_data.append({
            "Index": len(coding_data),  # Add an index starting from 0
            "Date": specific_date.strftime("%d/%m/%y"),
            "Day": day,
            "Total Hours": hours
        })

    # Display weekly summary
    total_weekly_hours = sum(entry["Total Hours"] for entry in coding_data)
    average_daily_hours = total_weekly_hours / len(coding_data)

    print("\nWeekly Summary:")
    print(f"Total Hours: {total_weekly_hours:.2f} hours")
    print(f"Average Daily Hours: {average_daily_hours:.2f} hours")
    print(f"Progress report: Your goal was to spend {goal_setting} hours learning to code. You spent {total_weekly_hours} hours!")

    if total_weekly_hours < goal_setting:
        print("You need to spend more time learning...")
    elif total_weekly_hours == goal_setting:
        print("Well done you met your goal this week! Keep it up!")
    elif total_weekly_hours > goal_setting:
        print("Woah! Going above and beyond this week. Keep this up and you will do very well.")
    else:
        print("Something went wrong.")

    # Saving the data to a CSV to use for later
    csv_filename = "total_tracked_coding_hours.csv"

    with open(csv_filename, mode='w', newline='') as file:
        fieldnames = ["Index", "Date", "Day", "Total Hours"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for entry in coding_data:
            writer.writerow(entry)

    print(f"\nCoding hours data saved to {csv_filename}.")

# Weekly data 
df = pd.read_csv('total_tracked_coding_hours.csv', parse_dates=['Date'], dayfirst=True)
df.set_index("Date", inplace=True)

weekly_summary = df.resample('W').sum() # Resamples the daily data into a week i.e. getting the total for the week. 


weekly_summary['Month'] = weekly_summary.index.month_name()

monthly_summary = weekly_summary.groupby('Month')['Total Hours'].sum()

weekly_summary_csv_filename = 'Weekly_summary.csv'
weekly_summary.to_csv(weekly_summary_csv_filename, columns=['Total Hours'])

monthly_summary = monthly_summary.reindex(months, fill_value=0)

# Plotting the bar chart

plt.xticks(rotation=45, ha='right')
plt.bar(monthly_summary.index, monthly_summary)
plt.title('Total Monthly Coding Hours')
plt.xlabel('Month')
plt.ylabel('Total Hours')
plt.show()

# print("\nWeekly Summary:")
# for index, row in weekly_summary.iterrows():
#     end_of_week = index + timedelta(days=6)  # Assuming Sunday is the last day of the week
#     print(f"Week ending {end_of_week.strftime('%Y-%m-%d')}: Total Hours - {row['Total Hours']:.2f} hours")

# Create a bar chart




main()