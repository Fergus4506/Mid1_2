grid=[1]
while True:
    try:
        n=int(input())
        l=n-len(grid)
        ans=0
        if l<=0:
            print(grid[n-1])
            for i in range(n):
                ans=ans+grid[i]
            print(ans)
        else:
            for i in range(len(grid)+1,n+1):
                grid.append(grid[i-2]*3+2)
            print(grid[n-1])
            for i in range(n):
                ans=ans+grid[i]
            print(ans)
    except:
        break
    