"""
A quadratic equation a x² + b x + c = 0 has either 0, 1, or 2 distinct solutions for real values of x.
Given a, b and c, you should return the number of solutions to the equation.
a will always be non-zero
"""


def solutionCounter(a, b, c):
    if a > 0:
        if (a * (-b / a) ** 2) + b * (-b / a) + c < 0:
            return 2
        elif (a * (-b / a) ** 2) + b * (-b / a) + c == 0:
            return 1
        else:
            return 0

    else:
        if (a * (-b / a) ** 2) + b * (-b / a) + c > 0:
            return 2
        elif (a * (-b / a) ** 2) + b * (-b / a) + c == 0:
            return 1
        else:
            return 0