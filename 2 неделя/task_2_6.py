L=[i for i in input()]
res = ""
for k in L:
    if L.count(k) == 1:
        res+=k
print(" ".join(res))    
