




# gets the total hours worked for 5 days
def get_hours_worked():
    days = 1
    days_worked = []
    hours_worked = []

    while days <= 5:
        hours = float(input(f"Enter the number of hours worked for Day #{days}: "))
        if hours < 0 or hours > 24:
            print("Invalid input. please enter a number between 0 and 24")
        else:
            days_worked.append(days)
            hours_worked.append(hours)
            days += 1
    return days_worked, hours_worked


def line_break():
    print("----------------------------------------------------------------------------")

 
# find the most hours worked in a single day, prints the number of hours worked and the day those hours were achieved.
def most_hours_in_day(days_worked, hours_worked):
    most_hours = max(hours_worked)
    print("The most hours worked was on:")

    for i in range(len(hours_worked)):
        if hours_worked[i] == most_hours:
            print(f"Day #{days_worked[i]} when you worked {most_hours:.0f} hours.")

# calculates the final hours as well as the average hours worked
def final_hours(hours_worked):
    final_hours = sum(hours_worked)
    average_hours = final_hours / len(hours_worked)

    print(f"The total number of hours worked was on: {final_hours:.0f} hours")
    print(f"The average hours worked per day was: {average_hours:.1f} hours")


# calculates days worked less than 7 hours
def days_slacked_off(days_worked, hours_worked):
    print("days you slacked off (i.e worked less than 7 hours):")

    for i in range(len(hours_worked)):
        if hours_worked[i] < 7:
            print(f"Day #{days_worked[i]:.0f}: {hours_worked[i]:.0f} hours")


# main function that calls the other functions
def main():
    days_worked, hours_worked = get_hours_worked()
    line_break()
    most_hours_in_day(days_worked, hours_worked)
    line_break()
    final_hours(hours_worked)
    line_break()
    days_slacked_off(days_worked, hours_worked)

# calls my main function
main()




