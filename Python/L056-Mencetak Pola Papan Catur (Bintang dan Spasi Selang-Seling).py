for i in range(1, 5 + 1):
    for j in range(1, 8 + 1):
        if (i + j) % 2 == 0:
            print("*", end="")
        else :
            print(" ", end="")
    print()