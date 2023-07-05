n,m=map(int,input().split())
grid=[[]for i in range(n)]
color=0
for i in range(m):
    t=list(map(int,input().split()))
    grid[t[0]-1].append([t[1]-1,color])
    grid[t[1]-1].append([t[0]-1,color])
    color=(color+1)%2

# print(grid)


queue=[]
queue.append([0,0,1,"0"])
maxchange=0
check=0
while len(queue):
    now=queue.pop(0)
    lastcolor=now[1]
    lastpass=now[3:]
    for i in range(len(grid[now[0]])):
        nowpass=lastpass[:]
        if str(grid[now[0]][i][0]) in nowpass:
            continue
        elif grid[now[0]][i][0]==n-1:
            # print(now)
            print(now[2]-1)
            check=1
            break
            # print(*now)
            # if lastcolor!=grid[now[0]][i][1]:
            #     if now[2]+1>maxchange:
            #         maxchange=now[2]+1
            # else:
            #     if now[2]>maxchange:
            #         maxchange=now[2]
            # continue
        # print(now)
        # print(grid[now[0]])
        nowpass.append(str(grid[now[0]][i][0]))
        t=[grid[now[0]][i][0],grid[now[0]][i][1],now[2]+1]+nowpass
        queue.append(t)
        # if lastcolor==-1:
        #     t=[grid[now[0]][i][0],grid[now[0]][i][1],0]+nowpass
        #     queue.append(t)
        # elif lastcolor!=grid[now[0]][i][1]:
        #     print("@")
        #     t=[grid[now[0]][i][0],grid[now[0]][i][1],now[2]+1]+nowpass
        #     queue.append(t)
        # else:
        #     t=[grid[now[0]][i][0],grid[now[0]][i][1],now[2]]+nowpass
        #     queue.append(t)
    if check:
        break
    # print(maxchange)
    #break
