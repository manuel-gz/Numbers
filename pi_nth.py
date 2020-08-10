#This program calculates pi using the Chudnovsky algorithm to the nth digit enter by the user
import numpy as np 
from decimal import Decimal, getcontext

print("I'll calculate pi to the nth number, please enter n")
n=int(input())
getcontext().prec=n
C = Decimal(426880*np.sqrt(10005))
L=13591409
M=1
X=1
K=6
suma=13591409
for i in range(1,100):
    M *= Decimal((K**3-16*K)/(K+1)**3)
    L += 545140134
    X *= -262537412640768000
    suma +=  M*L/X
    K += 12
pi= C/suma
print("pi to the ",n ,"th digit is ", pi)