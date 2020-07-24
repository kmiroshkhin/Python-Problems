'''
Write a function that returns True if two lists, when combined, form a consecutive sequence.

Examples
consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True

consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False

consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) ➞ False

consecutive_combo([44, 46], [45]) ➞ True
'''

def consecutiveSequence(a,b):
    jointArray=[]
    for i in a:
        jointArray.append(i)
    for i in b:
        jointArray.append(i)
    jointArray.sort(reverse=False)
    print(jointArray)

    consecutive = True;counter=0;prior = min(jointArray)

    for i in jointArray:
        if counter == 0:
            prior = i
            counter = 1
        else:
            if (i-1 != prior):
                print(prior,i)
                consecutive = False
                continue
            else:
                prior = i
                counter+=1

    return consecutive
