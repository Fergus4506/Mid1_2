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
queue.append([0,1,"0"])
check=0
while len(queue):
    now=queue.pop(0)
    lastpass=now[2:]
    for i in range(len(grid[now[0]])):
        nowpass=lastpass[:]
        if str(grid[now[0]][i]) in nowpass:
            continue
        elif grid[now[0]][i]==n-1:
            # print(now)
            print(now[1]-1)
            check=1
            break
        nowpass.append(str(grid[now[0]][i]))
        t=[grid[now[0]][i],now[1]+1]+nowpass
        queue.append(t)
    if check:
        break
