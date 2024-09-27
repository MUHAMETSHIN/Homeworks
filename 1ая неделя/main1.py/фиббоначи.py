a=[1, 1]
N=int(input())
for i in range(N-2):
    z=a[len(a)-1] + a[len(a)-2]
    a.append(z)
print(a[len(a)-1])