n=int(input())
for i in range(n):
    k=int(input())
    check=1
    for j in range(k):
        t,tp=map(int,input().split())
        check*=t**tp
    