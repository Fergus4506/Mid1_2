import queue
import math
import time
start_time = time.time()
# 執行一些程式碼


def spfa(grid,start):
    myQueue=[start-1]
    dis=[float("inf") for i in range(len(grid))]
    # print(dis)
    dis[start-1]=0
    while len(myQueue)!=0:
        now=myQueue.pop(0)
        for i in range(len(grid)):
            if (grid[now][i]+dis[now]>dis[i] and grid[now][i]+dis[now]!=float("inf")) or (dis[i]==float("inf") and grid[now][i]+dis[now]!=float("inf")):
                dis[i]=grid[now][i]+dis[now]
                myQueue.append(i)
    return dis
 
count=0
while 1:
    count+=1
    if count>1:
        print()
    n=int(input())
    if n==0:
        break
    start=int(input())
    st=start
    grid=[[float("inf")]*n for i in range(n)]
    # print(grid)
    while 1:
        s,e=map(int,input().split())
        if s==e:
            break
        grid[s-1][e-1]=1
    ans,pos=0,0
    temp=spfa(grid,start)
    for i in range(n):
        if temp[i]>ans and temp[i]!=float("inf"):
            ans=temp[i]
            pos=i
    if ans==0:
        print("Case %d: The longest path from %d has length %d, finishing at %d."%(count,st,ans,start))
    else:
        print("Case %d: The longest path from %d has length %d, finishing at %d."%(count,st,ans,pos+1))
end_time = time.time()
execution_time = end_time - start_time
print(execution_time,"s")