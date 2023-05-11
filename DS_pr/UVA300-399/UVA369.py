grid=[1]
for i in range(2,101):
    grid.append(grid[len(grid)-1]*i)
#print(len(grid))
while True:
    temp=list(map(int,input().split()))
    if temp[0]==0 and temp[1]==0:
        break
    N,M=temp[0],temp[1]
    if temp[0]==temp[1]:
        print("%d things taken %d at a time is 1 exactly."%(N,M))
    else:
        print("%d things taken %d at a time is %d exactly."%(N,M,grid[N-1]//(grid[N-M-1]*grid[M-1])))
