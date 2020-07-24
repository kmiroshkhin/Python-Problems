"""
Create a function that takes a list of numbers between 1 and 10 (excluding one number) and returns the missing number.
"""

def missing_num(lst):
    lst.sort()
    last=min(lst)
    for i in lst:
        if (i!=last) and (i-1!=last):
            return(i-1)
        else: last=i



