f=open('input.txt', 'r')
h=open('output.txt', 'w')
A=f.readlines()
B = list(map(int, A[0].split()))
op=1
sm=0
print(A[1])
if A[1] == '*':
    for i in B:
        op *= i
    h.write(str(op))
if A[1] == '-':
    for i in B:
        sm -= i
    h.write(str(sm))
if A[1] == '+':
    for i in B:
        sm += i
    h.write(str(sm))
f.close()
h.close()
