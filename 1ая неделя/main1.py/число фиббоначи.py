n=int(input())
if n == 0:
    print(1)
else:
    def fibbo(n):
        if  n == 1 or n==2:
            return 1

        res = fibbo(n-1) + fibbo(n-2)
        return res
    print(fibbo(n))    