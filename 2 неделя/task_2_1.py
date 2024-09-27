ch=list(map(int, input().split()))
n=ch[0]*0.5*(ch[0]+1)
#print(n)#проверка
#print(sum(ch[1:]))#проверка
print(int(n-(sum(ch[1:]))))