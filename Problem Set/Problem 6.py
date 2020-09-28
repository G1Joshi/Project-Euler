def sqrofsum(n):
    sum=0
    for i in range(n+1):
        sum+=i
    return sum*sum

def sumofsqr(n):
    sum=0
    for i in range(n+1):
        sum+=i*i
    return sum

n=100
print(sqrofsum(n)-sumofsqr(n))
