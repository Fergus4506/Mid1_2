def DFScheck(grid,nowtime,minsum,nowsum):
    print(nowtime,minsum,nowsum)
    if len(grid)==0:
        # print(minsum)
        return nowsum
    else:
        for i in range(len(grid)):
            temp=grid[:]
            if (grid[i][0]+nowtime)*grid[i][1]+nowsum<minsum:
                nexttime=nowtime+grid[i][0]
                nextsum=(grid[i][0]+nowtime)*grid[i][1]+nowsum
                
                temp.pop(i)
                minsum=DFScheck(temp,nexttime,minsum,nextsum)
    return minsum
while 1:
    try:
        n=int(input())
        grid1=list(map(int,input().split()))
        grid2=list(map(int,input().split())) 
        grid=[[i,j] for i,j in zip(grid1,grid2)]
        print(DFScheck(grid,0,float('inf'),0))
    except EOFError:
        break