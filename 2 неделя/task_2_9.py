f= open('input_9.txt', 'r')
a = f.readlines()
count = 0
for i in range(len(a)):
    c_dot = a[i].count(".")
    c_vop = a[i].count("?")
    c_vos = a[i].count('!')
    c_mndot = a[i].count('...')
    c_vosp = a[i].count('?!')
    count += ((c_dot - c_mndot*3) + (c_vop - c_vosp) + (c_vos - c_vosp) + c_mndot + c_vosp) #с формулой для вычисления кол-ва разделителей помог Динар
print(count)