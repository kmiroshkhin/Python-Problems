'''
Create a function that takes a single character as an argument and
returns the char code of its lowercased / uppercased counterpart.
'''

def counterpartCharCode(char):
    if char.isupper():
        char = char.lower()
        return ord(char)
    else:
        char = char.upper()
        return ord(char)

