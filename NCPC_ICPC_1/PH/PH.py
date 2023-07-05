n,m=map(int,input().split())
grid=[[]for i in range(n)]
color=0
for i in range(m):
    t=list(map(int,input().split()))
    grid[t[0]-1].append(t[1]-1)
    grid[t[1]-1].append(t[0]-1)
    color=(color+1)%2

# print(grid)


queue=[]
queue.append(0)
np=[]
ans=1
check=0
while len(queue):
    zz=queue
    for x in range(len(zz)):
        now=zz.pop(0)
        for i in range(len(grid[now])):
            if grid[now][i] in np:
                continue
            elif grid[now][i]==n-1:
                # print(now)
                print(ans-1)
                check=1
                break
            np.append(grid[now][i])
            queue.append(grid[now][i])
        if check:
            break
    ans+=1
    if check:
        break
