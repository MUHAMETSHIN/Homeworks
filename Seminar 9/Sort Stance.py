#Распределим приоритеты операторов
def rating(op):
    if op == '(':
        return -19
    if op == '-':
        return 1
    if op == '+':
        return 0
    if op == '/':
        return 3
    if op == '*':
        return 2
def calc(s):
    operators = ['+', '-', '*', '/']
    inpt = s.split() #вход
    stack = [] #стек
    outpt = [] #выход
    finish = ''
    for i in inpt:
        if i not in operators: #закидываю числа сразу в выход
            outpt.append(i)
        if i == '(':
            stack.append(i)

        if i in operators:
            if stack == []:
                stack.append(i)
            else:
                while stack and rating(i) <= rating(stack[-1]):  
                    outpt.append(stack.pop())
                stack.append(i)
        if i == ')':
            while stack and stack[-1] != '(':
                outpt.append(stack.pop())
            outpt.append(stack.pop())
            
            

    #после того, как пройдемся по всем элементам во входе, оставшиеся операторы закинем в выход
    outpt += stack[::-1]
    #делаем красиво, удаляем скобки и возвращаем готовую строку
    for t in outpt:
        z = ['(', ')']
        if t not in z:
            finish = finish + t + ' '

    return finish



s = input()
print(calc(s))
            

