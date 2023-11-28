while 1:
    try:
        n,k=map(int,input().split())
        grid=list(map(int,input().split()))
        dpgrid=[0 for i in range(n)]
        # print(len(grid),len(dpgrid))
        ans=0
        for i in range(n-1,-1,-1):    
            if i+grid[i]>=n:
                dpgrid[i]=1
            else:
                dpgrid[i]=dpgrid[grid[i]+i]+1
            if dpgrid[i]<=k:
                ans+=1
        print(ans)
    except EOFError:
        break