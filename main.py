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

import datetime
import csv

# This section gets the user to input their time spent learning to code during the week and then saves it to a CSV file for later

def main():
    # Initialize variables
    coding_data = []
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

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
        current_date = datetime.datetime.now()
        day_of_week = days_of_week.index(day)
        delta_days = (current_date.weekday() - day_of_week) % 7
        specific_date = current_date - datetime.timedelta(days=delta_days)

        # Check if the calculated date is in the future
        if specific_date > current_date:
            print(f"Please enter a valid time for {day}. The date for {day} has not occurred yet.")
            continue

        coding_data.append({
            "Index": len(coding_data) + 1,  # Add an index starting from 1
            "Date": specific_date.strftime("%a %d/%m/%y"),
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

if __name__ == "__main__":
    main()

# The user has now entered the data and it is now saved to a CSV
# The next step is to plot this data to a graph that updates itself each time the user logs/inputs new data/ hours learning
# The graph should plot the goal hours and the time actually spent learning to code. 

# # from datetime import datetime
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib import style 

# import calendar 

# style.use('ggplot')

# # Calendar 
# def display_calendar(year, month):
#     # Generate a calendar for the specified year and month
#     cal = calendar.monthcalendar(year, month)

#     # Define the days of the week
#     weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

#     # Display the header
#     print(f"{' '.join(weekdays)}")

#     # Display each week in the calendar
#     for week in cal:
#         week_str = " ".join(str(day) if day != 0 else "  " for day in week)
#         print(week_str)

# if __name__ == "__main__":
#     # Get user input for the year and month
#     year = int(input("Enter the year: "))
#     month = int(input("Enter the month (1-12): "))

#     # Display the calendar
#     display_calendar(year, month)

# # Todays Date
# def get_todays_date():
#     current_datetime = datetime.now()
#     formatted_date = current_datetime.strftime('%d/%m/%Y %A')
#     return formatted_date

# if __name__ == "__main__":
#     formatted_date = get_todays_date()
#     print("Today's date: ", formatted_date)

#     # Daily goal setter
#     daily_goal = float(input("How many hours a day are you going to code? "))

#     # y = daily_goal

#     # Ask the user for daily learning hours
#     user_daily_hours = float(input("How many hours did you spend learning to code today? "))

#     # y2 = user_daily_hours

#     # x = ['Mon','Tues','Wed','Thu','Fri','Sat','Sun']
#     # plt.bar(x, y, label='Goal', color='r')
#     # plt.bar(x, y2, label='Learning', color='b')

#     # plt.show()

#     # Example: Display daily progress and goal
#     daily_progress = min(user_daily_hours, daily_goal)
#     print(f"Today's Progress: {daily_progress}/{daily_goal} hours")

#     # Example: Display health bar visualization
#     progress_bar = "#" * int((daily_progress) * 10)
#     print("Progress Bar:", progress_bar)


# # user_daily_hours = int(input("How many hours this week are you planning on learning to code? "))