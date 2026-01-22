rows = 5
cols = 4
for i in range(rows):
    for j in range(cols):
        if i == 0 or i == 2 or i == 4 or j == 0 or j == 3:
            print("#", end=" ")
        else:
            print("*", end=" ")
    print()