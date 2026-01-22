n = 5  
mid = n // 2 

for i in range(n):
    for j in range(n):
        distance = abs(i - mid) + abs(j - mid)
        
        if distance == 1 or (i == mid and j == mid):
            if i == mid and j == mid:
                print("0", end=" ")
            else:
                print("1", end=" ")
        else:
            print("0", end=" ")
            
    print()