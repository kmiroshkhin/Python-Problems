"""
Create a function that counts how many characters make up a rectangular shape. You will be given a list of strings.
"""

def count_characters(lst):
    m=0
    for i in lst:
        for n in i:
            m=m+1
    return m

print(count_characters(['abc','def','xyz']))