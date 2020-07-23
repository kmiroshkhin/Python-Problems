"""
Create a function that returns True if the given string has any of the following:

Only letters and no numbers.
Only numbers and no letters.
If a string has both numbers and letters, or contains characters which don't fit into any category, return False

"""

def AlphaNumeric(Feed):
    list=[]
    for i in Feed:
        try: i = int(i)
        except:
            None
        if type(i) not in list:
            list.append(type(i))
    if len(list) > 1:
        return False
    else:
        return True



