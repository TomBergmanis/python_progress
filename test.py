import matplotlib.pyplot as plt

def get_weekly_totals(hours_per_day):
    weekly_totals = []
    total_hours = 0

    for hours in hours_per_day:
        total_hours += hours
        if len(weekly_totals) % 7 == 6:  # end of the week
            weekly_totals.append(total_hours)
            total_hours = 0
        else:
            weekly_totals.append(None)

    return weekly_totals

def plot_bar_graph(months, weekly_totals, month_names):
    weeks = list(range(1, len(weekly_totals) + 1))
    bar_width = 0.2

    for i, month in enumerate(months):
        plt.bar(
            [week + i * bar_width for week in weeks],
            weekly_totals[i::len(months)],
            bar_width,
            label=month_names[i]
        )

    plt.xlabel('Weeks')
    plt.ylabel('Total Hours')
    plt.title('Total Time Spent Learning to Code Each Week')
    plt.xticks([week + bar_width * (len(months) - 1) / 2 for week in weeks],
               [f'Week {week}' for week in range(1, len(weekly_totals) + 1)])
    plt.legend()
    plt.show()

def main():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Example data: hours spent learning to code each day of the week for each month
    hours_per_day = [
        # Example: Jan
        2, 3, 4, 5, 1, 2, 3,  # Week 1
        1, 2, 3, 4, 2, 3, 4,  # Week 2
        # ... (repeat for each month)
    ]

    weekly_totals = get_weekly_totals(hours_per_day)
    plot_bar_graph(months, weekly_totals, month_names)

if __name__ == "__main__":
    main()
