"""Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list. If Bob is not in the array, return -1.

Examples
find_bob(["Jimmy", "Layla", "Bob"]) ➞ 2

find_bob(["Bob", "Layla", "Kaitlyn", "Patricia"]) ➞ 0

find_bob(["Jimmy", "Layla", "James"]) ➞ -1
"""

def find_bob(names):
    counter = -1;encounterBob=False
    for name in names:
        if name =='Bob':
            counter += 1
            encounterBob=True
            break
        elif name !='Bob':
            counter += 1
    if encounterBob == True:
        return counter
    else:
        return -1
