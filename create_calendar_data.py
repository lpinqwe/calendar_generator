import calendar
from datetime import datetime


class create_calendar_data:
    year = 0
    month = 1
    week = "Mo Tu We Th Fr Sa Su"
    label = ''
    day_arr = []
    calendar_arr = []

    def __init__(self):
        current_date = datetime.now()
        self.month = current_date.month
        self.year = current_date.year

    def set_data(self, month_int, year_int):
        self.year = year_int
        self.month = month_int

    def create_lables(self):
        a = calendar.month(self.year, self.month)
        calendar_arr = a.split("\n")
        self.calendar_arr=calendar_arr
        self.label = calendar_arr[0].strip()
        print(self.label)
        self.day_arr = a[2:]

    def get_label(self):
        return self.label

    def get_month_arr(self):
        return self.calendar_arr

    def get_day_arr(self):
        return self.day_arr

    def get_week(self):
        return self.week
