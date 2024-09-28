L=list(input().split()) 
for i in range(0, len(L)-1, 2): 
    L[i], L[i+1]= L[i+1], L[i]
print(' '.join(L))    