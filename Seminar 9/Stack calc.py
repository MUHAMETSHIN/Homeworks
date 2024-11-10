flag = True
while flag:
    def calc(s):
        a = s.split()
        stack = []
        operators = ['+', '-', '*', '/']
        for i in range(len(a)):
            if a[i] not in operators:
                stack.append(a[i])  
            else:
                try:
                    second = stack.pop()
                    first = stack.pop()
                except:
                    print('Ошибка, БРО!')
                    return
                stack.append(str(eval(first + a[i] + second)))
        return stack[0]
    s = input()  
    print(calc(s))
    if s == 'Stop':
        flag == False

