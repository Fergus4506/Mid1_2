import math
n=int(input())
for i in range(n):
    m,n = map(int,input().split())
    print(((n-1)+(n-m))*m//2)