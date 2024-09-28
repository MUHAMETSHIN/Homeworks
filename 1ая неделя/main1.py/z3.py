A = list(map(int, input().split()))
pr=1
for i in A:
    pr=pr*i
print(pr**(1/len(A)))    


