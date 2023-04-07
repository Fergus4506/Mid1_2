n=int(input())
for i in range(n):
    s,e=map(int,input().split())
    ans=0
    for j in range(s,e+1):
        temp=0
        for x in range(2,j):
            if j%x==0:
                temp+=1
        if temp>ans:
            ans=temp