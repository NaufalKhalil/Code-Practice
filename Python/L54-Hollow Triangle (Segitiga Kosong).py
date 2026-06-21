for i in range(1, 5 + 1):
    for j in range(1, i + 1):
        if j == 1 or i == j or i == 5:  
            print("*", end="")
        else :
            print(" ", end="")
    print()