"""Python Progress tracker 
    Allows the user to track how much time they spent per day learning to code
    This could be done by taking the input of the user for each day and then this fills a bar
    the user could set a goal in terms of hours studying and then can track whether they have achieved it
    They then could have a sort of graph / UI that shows over the year how much time they spent learning to code
    this also seeing where they spent more time than others"""

""""
A way of knowing the actual date each time the project is opened. 
Calendar with a week view 
user input on their goal in terms of hours per day
user input on their goal in terms of hours per week 
A section showing the amount of time spent each day as a sort of health bar which increases as the user enters more time 
mile stones - motivational messages after a certain amount of time dedicated to learnign coding
a graph overview of the Week, Month and Year.

Track Daily Learning Hours:
Allow the user to input the number of hours they spent learning to code each day.
Update a variable or data structure to store this information for each day.
Display Weekly Goals:
Ask the user for their weekly learning goal in terms of hours.
Display the goal and the progress in a user-friendly way.
Health Bar Visualization:
Create a visualization (like a progress bar) to represent the amount of time the user has spent compared to their weekly goal.
Update the visualization each time the user adds their daily learning hours.
Milestones and Motivational Messages:
Implement milestones to provide motivational messages when the user reaches certain milestones (e.g., 10 hours, 20 hours, etc.).
Graph Overview:
Utilize a library like Matplotlib to create a graph overview of the user's learning time.
Plot weekly, monthly, and yearly views based on the stored data.

could add a stop watch timer that records how long you are coding for. this could then replace the user's input on the amount of time spent learning

"""

import csv
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
from matplotlib import style 

style.use('ggplot')

# This section gets the user to input their time spent learning to code during the week and then saves it to a CSV file for later

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

# The user has now entered the data and it is now saved to a CSV
# The next step is to plot this data to a graph that updates itself each time the user logs/inputs new data/ hours learning
# The graph should plot the goal hours and the time actually spent learning to code. 

# Shows the amount of time in a week spent learning to code
def plot_weekly_summary(df):
  
    fig, axis = plt.subplots(1,1)

    # Set the width of each bar
    bar_width = 0.35

    # Set the position of bars on X-axis
    bar_positions_actual = np.arange(len(df.index))
    bar_positions_goal = bar_positions_actual + bar_width

    # Plotting the actual time spent learning
    axis.bar(bar_positions_actual, df['Total Hours'], label='Actual Time', width=bar_width, color='green', alpha=0.9)

    # Plotting the goal time for each day
    goal_hours = [goal_setting / 7] * len(df.index)
    axis.bar(bar_positions_goal, goal_hours, label='Goal Time', width=bar_width, color='orange', alpha=0.6)

    set_date = df.index.strftime('%d/%m/%y\n%A')

    plt.xticks((bar_positions_actual + bar_positions_goal) / 2, set_date, rotation=45)
    plt.xlabel('Date')
    plt.ylabel('Hours')
    plt.title('Coding Hours vs. Goal Hours')
    # Adding a legend to differentiate between Actual Time and Goal Time
    plt.legend()
    plt.subplots_adjust(left=0.083, bottom=0.238, right=0.94, top=0.936, wspace=0.2, hspace=0)

    # plt.show()

# Monthly Tracker done by week 
    
# def plot_monthly_summary(df):
#     df['Week'] = df.index.strftime('%U')
#     weekly_summary = df.groupby(['Month', 'Week'])['Total Hours'].sum()

#     fig, axis = plt.subplots(1,1)   
#     bar_positions = np.arange(len(weekly_summary))

#     axis.bar(bar_positions, weekly_summary, color='purple', alpha=0.7)

#     # Use multi-level labels for better readability
#     labels = [f'Month {month}, Week {week}' for (month, week) in weekly_summary.index]
#     plt.xticks(bar_positions, labels, rotation=45, ha='right')

#     plt.xlabel('Weekly Breakdown')
#     plt.ylabel('Hours')
#     plt.title('Monthly Coding Hours Summary')

#     plt.show()


# Yearly tracker done by the week 
    
# def plot_yearly_summary(df):
#     df['Week'] = df.index.strftime('%U')
#     weekly_summary = df.groupby('Week')['Total Hours'].sum()

#     fig, axis = plt.subplots(1,1)
#     bar_positions = np.arange(len(weekly_summary))

#     axis.bar(bar_positions, weekly_summary, color='green', alpha=0.7)

#     plt.xlabel('Week')
#     plt.ylabel('Hours')
#     plt.title('Yearly Coding Hours Summary')

#     plt.show()

if __name__ == "__main__":
    main()

    # Reloads the CSV file to include the new data
    df = pd.read_csv('total_tracked_coding_hours.csv', parse_dates=['Date'], dayfirst=True)
    df.set_index("Date", inplace=True)

    plot_weekly_summary(df)

    # plot_monthly_summary(df)

    # plot_yearly_summary(df)



