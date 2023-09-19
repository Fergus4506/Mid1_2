def BFSpass(grid):
    ans=0
    queue=[]
    queue.append([0,0,0])
    if grid[0][0]==-1:
        return 0
    else:
        while len(queue)!=0:
            now=queue.pop(0)
            if now[0]==len(grid)-1 and now[1]==len(grid[0])-1:
                ans+=1
            if now[0]+1<len(grid) and grid[now[0]+1][now[1]]!=-1:
                queue.append([now[0]+1,now[1],now[2]+1])
            if now[1]+1<len(grid[0]) and grid[now[0]][now[1]+1]!=-1:
                queue.append([now[0],now[1]+1,now[2]+1])
    return ans
            



cs=int(input())
for i in range(cs):
    W,N=map(int,input().split())
    grid=[[0]*N for j in range(W)]
    for j in range(W):
        t=list(map(int,input().split()))
        for z in range(1,len(t)):
            grid[t[0]-1][t[z]-1]=-1
    print(BFSpass(grid))
    