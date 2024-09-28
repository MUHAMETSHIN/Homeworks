f= open('input3.txt', 'r')
t = open('output3.txt', 'w')
strnum = f.readline().split()
op = f.readline().strip()
b = f.readline().strip()
b = int(b)
for i in range(len(strnum)):  #перевод в 10чную СС при помощи int
        strnum[i] = int(strnum[i], b)
oper=1
sm=0
x_s = []
if  op == '*':
    for i in strnum:
        oper *= i
    while oper:
        num = oper % b
        x_s += str(num)
        oper = oper // b
    t.write(''.join(x_s[::-1]))
if op == '-':
    for i in strnum:
        sm -= i
    while sm:
        num = sm % b
        x_s += str(num)
        sm = sm // b
    t.write(''.join(x_s[::-1]))
if op  == '+':
    for i in strnum:
        sm += i
    while sm:
        num = sm % b
        x_s += str(num)
        sm = sm // b
    t.write(''.join(x_s[::-1]))
f.close()
t.close()