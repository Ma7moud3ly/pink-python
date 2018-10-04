def fact(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

def fact2(n):
    num = 1
    for i in range(1,n+1):
        num = num * i
    return num

