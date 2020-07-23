"""In this challenge, establish if a given integer num is a Curzon number.
If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.
Given a non-negative integer num,
implement a function that returns True if num is a Curzon number, or False otherwise.\
"""

def CurzonNumber(n):
    if (1+2**n)%(1+2*n)==0:
        print(n, " is a CurzonNumber")
        return True
    else:
        print(n, " is not a CurzonNumber")
        return False

