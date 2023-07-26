ans=0
def check(grid,end,now):
    Jlast,Jcount=-1,0
    Hlast,Hcount=-1,0
    for i in range(4):
        Jcount,Hcount=0,0
        for j in range(4):
            if grid[i][j]==Jlast:
                Jcount+=1
            else:
                Jlast=grid[i][j]
                Jcount=1
            if grid[j][i]==Hlast:
                Hcount+=1
            else:
                Hlast=grid[j][i]
                Hcount=1
            if Jcount==3 and now[0]==end[0] and now[1]==end[1]:
                return Jlast
            elif Hcount==3:
                return Hlast
    print("@")
    if grid[2][0]==grid[1][1]==grid[0][2]!=0:
        if now[0]==end[0] and now[1]==end[1]:
            return grid[2][0]
        else:
            return -1
    elif grid[3][0]==grid[2][1]==grid[1][2]!=0:
        if now[0]==end[0] and now[1]==end[1]:
            return grid[3][0]
        else:
            return -1
    elif grid[2][1]==grid[1][2]==grid[0][3]!=0:
        if now[0]==end[0] and now[1]==end[1]:
            return grid[2][1]
        else:
            return -1
    elif grid[3][1]==grid[2][2]==grid[1][3]!=0:
        if now[0]==end[0] and now[1]==end[1]:
            return grid[3][1]
        else:
            return -1
    elif grid[1][0]==grid[2][1]==grid[3][2]!=0:
        if now[0]==end[0] and now[1]==end[1]:
            return grid[1][0]
        else:
            return -1
    elif grid[0][0]==grid[1][1]==grid[2][2]!=0:
        if now[0]==end[0] and now[1]==end[1]:
            return grid[0][0]
        else:
            return -1
    elif grid[1][1]==grid[2][2]==grid[3][3]!=0:
        if now[0]==end[0] and now[1]==end[1]:
            return grid[1][1]
        else:
            return -1
    elif grid[0][1]==grid[1][2]==grid[2][3]!=0:
        if now[0]==end[0] and now[1]==end[1]:
            return grid[0][1]
        else:
            return -1

    return 0
def DFS(end,color,grid):
    global ans
    for i in range(4):
        for j in range(4):
            if grid[i][j]==0:
                grid[i][j]=color
                now=[i,j]
                ck=check(grid,end,now)
                if ck==2:
                    ans+=1
                elif ck==0:
                    DFS(end,(color+1)%2+1,grid)
                grid[i][j]=0
        print(grid,ans)
        

start=[1,int(input())]
end=list(map(int,input().split()))
grid=[[0]*4 for i in range(4)]
grid[start[0]][start[1]]=1
DFS(end,2,grid)
print(ans)

