n=int(input())
for i in range(n):
    mun=int(input())
    grid=list(map(int,input().split()))
    ans=0
    for j in range(mun):
        temp=grid[:j+1]
        temp.sort()
        # print(*temp)
        if (j+1)%2==0:
            ans+=(temp[(j+1)//2]+temp[(j+1)//2-1])//2
        else:
            ans+=temp[(j+1)//2]
    print(ans)