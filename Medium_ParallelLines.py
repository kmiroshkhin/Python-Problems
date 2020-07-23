"""Given two lines, determine whether or not they are parallel.

Lines are represented by a list [a, b, c], which corresponds to the line ax+by=c.

Examples
lines_are_parallel([1, 2, 3], [1, 2, 4]) ➞ True
# x+2y=3 and x+2y=4 are parallel.

lines_are_parallel([2, 4, 1], [4, 2, 1]) ➞ False
# 2x+4y=1 and 4x+2y=1 are not parallel.

lines_are_parallel([0, 1, 5], [0, 1, 5]) ➞ True
# Lines are parallel to themselves.
Notes
Two lines are parallels if they have the same slope and the y-intercepts are different. If the slopes are different, the lines are not parallel.
All test cases use valid input (no lists of the wrong size, for example).
All coefficients will be integers (whole numbers).
"""

def parallelTest(a,b):
    try:
        a1=a[0];b1=a[1];c1=a[2]
        a2=b[0];b2=b[1];c2=b[2]

        if a1/b1 == a2/b2:
            return 'true'
        else:
            return 'false'

    except:
        print('wrong format')
