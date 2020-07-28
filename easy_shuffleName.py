'''
switch first and last name

example:
Barack Obama --> Obama Barack
'''

def name_shuffle(txt):
    txt=txt.split()
    a=txt[0];b=txt[1]
    return b+" "+a

