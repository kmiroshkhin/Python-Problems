"""
Imagine a circle and two squares: a smaller and a bigger one. For the smaller one, the circle is a circumcircle and for the bigger one, an incircle.

Create a function, that takes an integer (radius of the circle) and returns the difference of the areas of the two squares.

"""

def TwoSquareVariance(radius):
    largeSquare = (2*radius)**2
    smallSquare = 2*radius**2
    variance = largeSquare - smallSquare
    return variance

print(TwoSquareVariance(7))
