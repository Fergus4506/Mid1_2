import math
def gcd(m, n):
    a = m
    b = n
    if n > m:
        m, n = n, m
    while m % n:
        k = n
        n = m % n
        m = k
    a=a//n
    b=b//n
    # print(a,b)
    if (a&1 and b&1):
        return n
    else:
        return 0

m,n=map(int, input().split())
# print(math.gcd(m,n))
print(gcd(m,n))