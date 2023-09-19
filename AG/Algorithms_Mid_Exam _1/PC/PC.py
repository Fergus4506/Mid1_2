T=int(input())
for i in range(T):
    if i:
        print()
    n=int(input())
    grid=[]
    for j in range(n):
        Id,S=input().split()
        grid.append([Id,int(S)])
    grid.sort(key=lambda x:x[0])
    grid.sort(key=lambda x:x[1],reverse=1)
    cnt=0
    pcnt=1
    last=0
    for j in range(n):
        cnt+=1
        if grid[j][1]!=last:
            pcnt=cnt 
            last=grid[j][1]
            print(pcnt,grid[j][0],grid[j][1])
        else:
            print(pcnt,grid[j][0],grid[j][1])
