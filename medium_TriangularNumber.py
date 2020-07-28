"""
This Triangular Number Sequence is generated from a pattern of dots that form a triangle. The first 5 numbers of the sequence, or dots, are:

1, 3, 6, 10, 15
This means that the first triangle has just one dot, the second one has three dots, the third one has 6 dots and so on.

Write a function that gives the number of dots with its corresponding triangle number of the sequence.

Examples
triangle(1) ➞ 1

triangle(6) ➞ 21

triangle(215) ➞ 23220
"""

def triangle(n):
    total=0
    new_row=0
    prior_row=1
    for i in range(n):
        if total ==0:
            prior_row = 1
            new_row = 1
            total = total + new_row
        else:
            new_row = prior_row + 1
            total = total + new_row
            prior_row = new_row
    return total
