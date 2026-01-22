rows = 5
cols = 5
for i in range(rows):
    for j in range(cols):
        if i == 0 or i == 2 or i == 4 or j == 0 or j == 2 or j == 4:
            print("#", end=" ")
        else:
            print("0", end=" ")
    print()