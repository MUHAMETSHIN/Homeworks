a = [int(i) for i in input().split()]
for k in range(len(a)):
    for j in range(len(a)):
        if k != j and a[k] == a[j]:
               break
    
    print(a[k], end=' ')