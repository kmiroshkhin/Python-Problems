"""
Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num up to length.
"""

def listOfMultiples(num,length):
    list=[]
    for i in range(1,length+1):
        list.append(num*i)
    return list

