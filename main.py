def add_daily_temp(temp_dict, temp_value, day_of_week):
    """
    Adds a daily temperature value to the given dictionary for a given day of the week.
    If the day already has a temperature value, the function does nothing.
    Returns the updated dictionary.
    """
    # check if the day already has a temperature value
    if day_of_week in temp_dict:
        print(f"Temperature for {day_of_week} already recorded.")
    else:
        # add the temperature value to the dictionary for the given day
        temp_dict[day_of_week] = temp_value
        print(f"Added temperature {temp_value} for {day_of_week}.")

    return temp_dict


























# create an empty dictionary
temps = {}

# add temperatures for Monday, Tuesday, and Wednesday
temps = add_daily_temp(temps, 72, "Monday")
temps = add_daily_temp(temps, 68, "Tuesday")
temps = add_daily_temp(temps, 75, "Wednesday")

# try to add a temperature for Tuesday again
temps = add_daily_temp(temps, 70, "Tuesday")

# display the resulting dictionary
print(temps)
















# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
