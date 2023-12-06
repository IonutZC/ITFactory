import calendar


class Calendar:
    def __init__(self, year):
        self.year = year
        self.cal = calendar.TextCalendar(calendar.SUNDAY)  # Set the start day of the week to Sunday

    def print_calendar(self, month):
        month_name = calendar.month_name[month]
        month_abbr = calendar.month_abbr[month]

        print(f"{month_name} {self.year}")
        print("Mo\tTu\tWe\tTh\tFr\tSa\tSu")

        month_calendar = self.cal.monthdayscalendar(self.year, month)

        for week in month_calendar:
            for day in week:
                if day == 0:
                    print("\t", end="")
                else:
                    print(f"{day}\t", end="")
            print()

    def get_day_of_week(self, day, month):
        weekday = calendar.weekday(self.year, month, day)
        return calendar.day_name[weekday]

    def get_days_in_month(self, month):
        return calendar.monthrange(self.year, month)[1]


# Example Usage
cal = Calendar(2022)
cal.print_calendar(10)  # Display the calendar for October 2022
print(cal.get_day_of_week(5, 10))  # Get the day of the week for October 5, 2022
print(cal.get_days_in_month(10))  # Get the number of days in October 2022
