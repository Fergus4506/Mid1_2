while 1:
    try:
        n,k=map(int,input().split())
        grid=list(map(int,input().split()))
        grid.sort()
        campare=[]
        for i in range(len(grid)-1):
            campare.append(grid[i+1]-grid[i])
        ans=0
        #print(*campare)
        campare.sort()
        for i in range(k):
            ans+=campare[i]
        print(ans)
    except EOFError:
        break