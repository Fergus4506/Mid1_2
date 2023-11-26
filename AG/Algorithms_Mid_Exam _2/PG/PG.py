count=0
def DFScheck(grid,now,ctype):
    grid[now[0]][now[1]]=2
    if now[0]-1>-1:
        if grid[now[0]-1][now[1]]==ctype:
            DFScheck(grid,[now[0]-1,now[1]],ctype)
    if now[0]+1<len(grid):
        if grid[now[0]+1][now[1]]==ctype:
            DFScheck(grid,[now[0]+1,now[1]],ctype)
    if now[1]-1>-1:
        if grid[now[0]][now[1]-1]==ctype:
            DFScheck(grid,[now[0],now[1]-1],ctype)
    if now[1]+1<len(grid[0]):
        if grid[now[0]][now[1]+1]==ctype:
            DFScheck(grid,[now[0],now[1]+1],ctype)
while 1:
    try:
        count+=1
        n,m=map(int,input().split())
        grid=[]
        for i in range(n):
            grid.append(list(map(int,input().split())))
        wans=0
        bans=0      
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    DFScheck(grid,[i,j],grid[i][j])
                    bans+=1
                elif grid[i][j]==0:
                    DFScheck(grid,[i,j],grid[i][j])
                    wans+=1
        print("Case #%d:"%(count))
        print("b: %d"%(bans))
        print("w: %d"%(wans))
        

    except EOFError:
        break