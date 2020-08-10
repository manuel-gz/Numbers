#"lazy" way to compute the nth fibonacci term 
import math 

def fibonacci(n):
    gr = (1 + 5 ** 0.5) / 2
    f = (gr**n-(1-gr)**n)/math.sqrt(5)
    return f

n = int(input("enter how many number you want to be displayed "))
print("here are the first ",n, "numbers of the fibonacci sequence ")
for i in range (0,n+1):
    print(fibonacci(i))



