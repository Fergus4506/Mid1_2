n=int(input())
grid=[]
for i in range(n):
    grid.append(int(input()))
check=1
for i in range(1,grid[len(grid)-1]+1):
    if i not in grid:
        check=0
        print(i)
if check:
    print("good job")