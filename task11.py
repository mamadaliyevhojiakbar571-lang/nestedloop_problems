rows = 5
cols = 5
counter = 0 

for i in range(rows):
    for j in range(cols):
        if counter % 4 == 0:
            print("0", end=" ")
        else:
            print("1", end=" ") 
        counter += 1 
    print() 