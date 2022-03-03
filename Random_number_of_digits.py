import random
def fun(n):
    if(n==0):
        return 0
    r= random.randint(10**(n-1),(10**n - 1))
    return r


n= int(input())

print(fun(n))
