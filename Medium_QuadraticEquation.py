"""
Create a function to find only the root value of x in any quadratic equation ax^2 + bx + c. The function will take three arguments:

a as the coefficient of x^2
b as the coefficient of x
c as the constant term
"""

def rootFinder(a,b,c):
    try:
        t = (b**2-4*a*c)**(1/2)
    except:
        return 'imaginary roots'
    root = (-b+t)/(2*a)
    return root


