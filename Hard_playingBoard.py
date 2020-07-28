"""
Create a function that takes in two parameters: rows, and columns, both of which are integers.
The function should then proceed to draw a playing board (as in the examples from the lectures)
the same number of rows and columns as specified. After drawing the board, your function should return True.

"""

def terminal_size():
    import os
    size = os.get_terminal_size
    return size[0],size[1]


def playBoard(x,y):
    rows = x*2 - 1
    columns = y*2 - 1

    for n in range(3,rows+3):
        if n%2 !=0:
            k=columns
            for m in range(1,columns+1):
                if m%2!=0 and k>(m):
                    print(" ",end="")
                elif m%2==0 and k>(m):
                    print("|",end="")
                else:
                    print(" ")
        else:
            print("-"*columns)

playBoard(8,16)