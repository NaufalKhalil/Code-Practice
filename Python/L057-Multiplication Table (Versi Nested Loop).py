for i in range(1, 5 + 1):
    for j in range(1, 5 + 1):
        if i * j < 10:
            print(" ", end="")

        print(i * j, end=" ")

    print()