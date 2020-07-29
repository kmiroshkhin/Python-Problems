"""
Create a function that returns true if a given inequality expression is correct and false otherwise.

Examples
correct_signs("3 < 7 < 11") ➞ True

correct_signs("13 > 44 > 33 > 1") ➞ False

correct_signs("1 < 2 < 6 < 9 > 3") ➞ True
"""

def correct_signs(txt):
    import re
    numbers=[];operator=[]
    numerics = re.split('<|>|=',txt)
    for i in range(len(numerics)):
        numerics[i]=int(numerics[i])
    operators = re.split('0|1|2|3|4|5|6|7|8|9',txt)
    for i in operators:
        if i != "": operator.append(i)

    accurate = True

    for i in range(len(operator)):
        if operator[i]==">":
            if numerics[i]>numerics[i+1]:
                continue
            else: accurate = False;break
        elif operator[i]=="<":
            if numerics[i]<numerics[i+1]:
                continue
            else: accurate = False;break
        elif operator[i]=="=":
            if numerics[i] == numerics[i+1]:
                continue
            else: accurate = False;break
    return accurate


print(correct_signs('12=12'))