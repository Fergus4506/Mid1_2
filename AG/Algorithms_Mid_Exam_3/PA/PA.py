while 1:
    n=int(input())
    if n==0:
        break
    else:
        grid=[]
        for i in range(n):
            temp=list(map(int,input().split()))
            grid.append(temp[1])
        grid.sort()
        ans=0
        if len(grid)%2==0:
            ans=grid[(len(grid)-1)//2]
        else:
            ans=grid[(len(grid))//2]
        print(ans,sum([abs(ans-i) for i in grid]))
