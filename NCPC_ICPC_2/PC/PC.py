P,D=map(int,input().split())
grid=[[0,0] for i in range(D)]
for i in range(P):
    temp=list(map(int,input().split()))
    grid[temp[0]-1][0]+=temp[1]
    grid[temp[0]-1][1]+=temp[2]

total=0
wa,wb=0,0
for i in range(D):
    total+=grid[i][0]
    total+=grid[i][1]
    if grid[i][0]>grid[i][1]:
        print("A",end=" ")
        wa+=grid[i][0]-((grid[i][0]+grid[i][1])//2+1)
        wb+=grid[i][1]
        print(grid[i][0]-((grid[i][0]+grid[i][1])//2+1),grid[i][1])
    else:
        print("B",end=" ")
        wa+=grid[i][0]
        wb+=grid[i][1]-((grid[i][0]+grid[i][1])//2+1)
        print(grid[i][0],grid[i][1]-((grid[i][0]+grid[i][1])//2+1))
print("%.10f"%(abs(wa-wb)/total))