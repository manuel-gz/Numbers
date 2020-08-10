def factorial(n)  :
    if n == 0:
        return 1
    else:
        a=1
        for i in range (1,n+1):
           a = a*i
        return(a)
n=int(input("enter the number you want to calculate: "))
print(n,"! is", factorial(n))