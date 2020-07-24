'''A set is a collection of unique items. A set can be formed from a list from removing all duplicate items.

[1, 3, 3, 5, 5, 5]
# original list

[1, 3, 5]
# original list transformed into a set
Create a function that sorts a list and removes all duplicate items from it.
'''

def setify(lst):
    newlst=[]
    for i in lst:
        if i not in newlst: newlst.append(i)
    return(newlst)
