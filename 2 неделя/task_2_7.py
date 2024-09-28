N = int(input())
a = [int(i) for i in input().split()]
cat = a[0]
for i in range(len(a)):
    if a.count(a[i]) >= a.count(cat):
        cat = a[i]
print(cat)    