"""
You work in a toy car workshop, and your job is to build toy cars from a collection of parts. Each toy car needs 4 wheels, 1 car body, and 2 figures of people to be placed inside. Given the total number of wheels, car bodies and figures available, how many complete toy cars can you make?

Examples
cars(2, 48, 76) ➞ 0
# 2 wheels, 48 car bodies, 76 figures

cars(43, 15, 87) ➞ 10

cars(88, 37, 17) ➞ 8
"""

def cars(wheels,bodies,figures):
    x=round(wheels/4-0.4999);y=round(bodies/1-0.4999); z=round(figures/2-0.49999)
    return min(x,y,z)
