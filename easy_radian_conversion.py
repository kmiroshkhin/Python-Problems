"""
Create a function that takes an angle in radians and converts it into degrees.

Examples
to_degree(math.pi) ➞ 180

to_degree(math.pi/2) ➞ 90

to_degree(math.pi/4) ➞ 45
"""

def to_degree(radian):
    import math
    return radian*180/math.pi

import math
print(to_degree(math.pi*2))
