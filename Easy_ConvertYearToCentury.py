"""
Write a function that takes a year and returns its corresponding century.
"""


def yearToCentury(year):
    century = (year-1)/100 +1
    century = int(century)
    return century

