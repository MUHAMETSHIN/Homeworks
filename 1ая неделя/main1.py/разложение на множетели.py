n=int(input())
prime_list=[]
key = True
def prime(n):
    while key == True:
        for i in range(n):
            if n%i == 0:
                prime_list.append(i)
                key == False
    prime(n//(prime_list[-1]))
            #prime_list.append(i)
            
    
print(prime_list)