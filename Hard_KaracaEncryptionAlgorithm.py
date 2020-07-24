"""
Make a function that encrypts a given input with these steps:

Input: "apple"

Step 1: Reverse the input: "elppa"

Step 2: Replace all vowels using the following chart:

a => 0
e => 1
i => 2
o => 2
u => 3

# "1lpp0"
Step 3: Add "aca" to the end of the word: "1lpp0aca"

Output: "1lpp0aca"
"""

def encrypt(word):
    reverse=""
    for i in word:
        reverse = i + reverse

    #vowel conversion dictionary
    condict ={"a":0,"e":1,"i":2,"o":2,"u":3}

    convert =""
    for i in reverse:
        if i in condict:
            convert += str(condict[i])
        else:
            convert += i

    convert +="aca"
    return convert

print(encrypt("apple"))