f= open('input_1.txt', 'r')
x = f.readlines()
x = list(map(int, x))
#first = x[1]
#x_10 = sum([b * first ** a for a, b in enumerate(x[::-1])])
x[0]=str(x[0])
x_10=int(x[0], x[1])
c=x[2]
x_s = ''
while x_10:
    num = x_10 % c
    x_s += str(num)
    x_10 = x_10 // c
print(x_s[::-1])
t=open('output_1.txt', 'w')
t.write(x_s[::-1])
f.close()
t.close()
