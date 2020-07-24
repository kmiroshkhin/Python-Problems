'''
Given the month and year as numbers, return whether that month contains a Friday 13th.

Examples
has_friday_13(3, 2020) ➞ True

has_friday_13(10, 2017) ➞ True

has_friday_13(1, 1985) ➞ False
'''


def FridayTheThirteen(month,year):
    import datetime
    if datetime.date(year,month,13).weekday()==4:
        return True
    else:
        return False
