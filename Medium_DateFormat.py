"""
Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.
"""

def formatConverter(Date):
    Month = str(Date[0:2])
    Day = str(Date[3:5])
    Year = str(Date[6:])
    NewDate = Year+Day+Month
    return NewDate


