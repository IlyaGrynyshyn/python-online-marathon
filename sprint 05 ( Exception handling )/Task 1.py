def day_of_week(day):
    week = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday',
    }
    error_num = "There is no such day of the week! Please try again."
    try:
        if isinstance(day, int):
            return (week.get(day, error_num))
        elif isinstance(day, str):
            return (week.get(int(day), error_num))

    except:
        return ("You did not enter a number! Please try again.")


print(day_of_week('9'))


