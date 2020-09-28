from math import sqrt

def isprime(n):
    for i in range(2, int(sqrt(n))+2):
        if n%i==0:
            return False
    return True

def prime(n):
    a=1
    num=2
    while True:
        if isprime(num):
            a+=1
        if a==n:
            return num
        num+=1
    
n=10001
print(prime(n))
