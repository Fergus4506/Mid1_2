while True:
    try:
        n=int(input())
        grid=[]
        for i in range(n):
            grid.append(list(map(float,input().split())))
        grid.sort(key=lambda x:x[1])
        grid.sort(key=lambda x:x[2],reverse=1)
        grid.sort(key=lambda x:x[3],reverse=1)
        for i in range(len(grid)):
            if i==len(grid)-1:
                print(int(grid[i][0]))
            else:
                print(int(grid[i][0]),end=" ")
    except EOFError:
        break