"""
Write a function that stutters a word as if someone is struggling to read it.
The first two letters are repeated twice with an ellipsis ... and space after each,
and then the word is pronounced with a question mark ?.
"""

def stutter(word):
    stutter ="";n=0
    for i in word:
        if n<2:
            stutter +=str(i)
            n+=1
        else:break
    return stutter+"... "+stutter+"... "+word+"?"

print(stutter('hello'))

