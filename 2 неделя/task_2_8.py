N = int(input())
a = [int(i) for i in input().split()]
for i in range(len(a)):
    sum = 0
    for j in range(len(a)):
        if a[j] < a [i]:
            sum += 1
    if sum == (len(a)/2)-0.5:
        print(a[i])
        break