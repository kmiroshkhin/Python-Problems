'''
Create a function that receives a non-negative integer and returns the factorial of that number.
'''

def factorialNumber(number):
    factorial = 1
    if number == 0:
        return factorial
    else:
        for i in range(1,number+1):
            factorial *= i
        return factorial
