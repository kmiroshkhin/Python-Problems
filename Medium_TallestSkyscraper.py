"""
A city skyline can be represented as a 2-D list with 1s representing buildings.
In the example below, the height of the tallest building is 4 (second-most right column).

[[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 0],
[0, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1]]
Create a function that takes a skyline (2-D list of 0's and 1's) and returns the height of the tallest skyscraper.
"""


def tallest_skyscraper(lst):
    skyscaper = [];k=0
    for m in lst:
        n=0
        for i in lst[n]:
            if k==0:
                skyscaper.append(i)
            else:
                skyscaper[n]=skyscaper[n]+lst[k][n]
            n=n+1
        k=k+1
    return max(skyscaper)

print(tallest_skyscraper([  [0, 0, 1, 0, 0, 0],
                            [0, 0, 1, 0, 1, 0],
                            [0, 0, 1, 0, 1, 0],
                            [0, 1, 1, 1, 1, 0],
                            [0, 1, 1, 1, 1, 0],
                            [1, 1, 1, 1, 1, 1]]))