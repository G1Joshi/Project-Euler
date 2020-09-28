def sqofsm(n):
    sum=0
    for i in range(n+1):
        sum+=i
    return sum*sum

def smofsq(n):
    sum=0
    for i in range(n+1):
        sum+=i*i
    return sum

n=100
print(sqofsm(n)-smofsq(n))
