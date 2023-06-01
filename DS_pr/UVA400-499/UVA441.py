def count(grid,now,pr,ct):
    if ct==6:
        print(*pr)
    else:
        for i in range(now,len(grid)):
            temp=pr[:]
            temp.append(grid[i])
            count(grid,i+1,temp,ct+1)
c=0
while True:
    n=list(map(int,input().split()))
    if n[0]==0:
        break
    if c:
        print()
    ps=n[0]
    gd=n[1:]
    count(gd,0,[],0)
    c=1
    