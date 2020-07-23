def PlayBoard(a, b):
    for row in range(a + 1):
        if row % 2 == 0:
            for column in range(b + 2):
                if column == b+1:
                    print(" ")
                else:
                    if column % 2 == 0:
                        print(" ", end="")
                    else:
                        print("|", end="")
        else:
            print("-" * (b+1))

PlayBoard(4,4)


x=5+4+5+(
    5
)
print(x)