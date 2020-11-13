def multiple(n):
    for i in range(1, 21):
        if n%i != 0:
            return 0
    return n

n=1
while(True):
    if multiple(n):
        print(n)
        break
    n+=1
