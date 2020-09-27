from math import sqrt

def isprime(n):
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True
    
def factor(num):
    i=int(sqrt(num))
    while i>0:
        if num%i==0:
            if isprime(i):
                return i
        i-=1

num=600851475143
print(factor(num))
