def ispalindrome(num):
    temp=num
    rev=0
    while temp:
        rev=rev*10+temp%10
        temp//=10
    return num == rev
    
def palindrome():
    lp=0
    a=999
    while a>99:
        b=999
        while b>99:
            c=a*b
            if c>lp and ispalindrome(c):
                lp=c
            b-=1
        a-=1
    return lp

print(palindrome())
