def copylist(grid):
    temp=[]
    for i in grid:
        t=[]
        for j in i:
            t.append(j)
        temp.append(t)
    return temp

def DFScheck(grid,now,nowans,maxans,nowtype,where):
    # print(now,where,nowtype,nowans,maxans)
    # for i in grid:
    #     print(*i)
    # print()
    if (nowtype==0 and where==1) or nowtype==1:
        for i in range(now[1]+1,len(grid[0])):
            temp=copylist(grid)
            if temp[now[0]][i]!=0:
                temp[now[0]][i]=nowtype
                if nowtype==0:
                    maxans=DFScheck(temp,[now[0],i],nowans+1,maxans,(nowtype+1)%2,1)
                else:
                    maxans=DFScheck(temp,[now[0],i],nowans,maxans,(nowtype+1)%2,1)
                break
    if (nowtype==0 and where==2) or nowtype==1:
        for i in range(now[1]-1,-1,-1):
            temp=copylist(grid)
            if temp[now[0]][i]!=0:
                temp[now[0]][i]=nowtype
                if nowtype==0:
                    maxans=DFScheck(temp,[now[0],i],nowans+1,maxans,(nowtype+1)%2,2)
                else:
                    maxans=DFScheck(temp,[now[0],i],nowans,maxans,(nowtype+1)%2,2)
                break
    if (nowtype==0 and where==3) or nowtype==1:
        for i in range(now[0]+1,len(grid)):
            temp=copylist(grid)
            if temp[i][now[1]]!=0:
                temp[i][now[1]]=nowtype
                if nowtype==0:
                    maxans=DFScheck(temp,[i,now[1]],nowans+1,maxans,(nowtype+1)%2,3)
                else:
                    maxans=DFScheck(temp,[i,now[1]],nowans,maxans,(nowtype+1)%2,3)
                break
    if (nowtype==0 and where==4) or nowtype==1:
        for i in range(now[0]-1,-1,-1):
            temp=copylist(grid)
            if temp[i][now[1]]!=0:
                temp[i][now[1]]=nowtype
                if nowtype==0:
                    maxans=DFScheck(temp,[i,now[1]],nowans+1,maxans,(nowtype+1)%2,4)
                else:
                    maxans=DFScheck(temp,[i,now[1]],nowans,maxans,(nowtype+1)%2,4)
                break
    return nowans if nowans>maxans else maxans

while 1:
    try:
        n,m=map(int,input().split())
        grid=[[1 for i in range(m)] for j in range(n)]
        grid[0][0]=0
        print(DFScheck(grid,[0,0],0,0,1,0))
    except EOFError:
        break