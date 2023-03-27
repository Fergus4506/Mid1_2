grid=[1]
while True:
    n=int(input())
    if n==-1:
        break
    if n+1<=len(grid):
        print(grid[n])
    else:
        for i in range(len(grid)-1,n):
            temp=grid[i]
            now=temp[0]
            count=0
            ans=""
            for j in grid:
                if j!=now:
                    ans=ans+str(count)+now
                    
