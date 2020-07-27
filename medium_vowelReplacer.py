"""Create a function that replaces all the vowels in a string with a specified character.

Examples
replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"

replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"

replace_vowels("shakespeare", "*") ➞ "sh*k*sp**r*"
"""

def replace_vowels(txt,ch):
    vowels = ['a','e','i','o','u'];replacementlist=[];replacement=""
    for i in txt:
        if i in vowels:
            replacementlist.append(ch)
        else:replacementlist.append(i)
    for i in replacementlist:
        replacement+=i
    return replacement


print(replace_vowels('Eurika!','#'))