def bbsort(grid,l):
    ans=0
    for i in range(l):
        # print(grid)
        for j in range(l-1,i,-1):
            if grid[j]<grid[j-1]:
                grid[j],grid[j-1]=grid[j-1],grid[j]
                ans+=1
    return ans
n=int(input())
for i in range(n):
    sl=int(input())
    grid=list(map(int,input().split()))
    print(bbsort(grid,sl))
