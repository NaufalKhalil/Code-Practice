for i in range (1, 5 + 1):

    for j in range(5 - i):
        print(" ", end="")
    
    for j in range((i * 2) - 1):
        print("*", end="")

    print()

for i in range(4, 0, -1 ):

    for j in range(5 - i):
        print(" ", end="")
    for j in range((i * 2) - 1):
        print("*", end="")
    
    print()