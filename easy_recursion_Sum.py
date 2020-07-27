"""Write a function that finds the sum of the first n natural numbers. Make your function recursive.

Examples
sum_numbers(5) ➞ 15
// 1 + 2 + 3 + 4 + 5 = 15

sum_numbers(1) ➞ 1

sum_numbers(12) ➞ 78
"""

def sum_numbers(n):
    addition=int()
    for i in range(1,n+1):
        addition+=i
    return addition
print(sum_numbers(5))