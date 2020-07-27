"""Write a function that returns the length of a string. Make your function recursive.

Examples
length("apple") ➞ 5

length("make") ➞ 4

length("a") ➞ 1

length("") ➞ 0
"""
def length(txt):
    n=0
    for i in txt:
        n+=1
    return (n)

print(length(''))