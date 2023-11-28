def test(grid):
    temp=grid[:]
    temp[0]=-1
    return temp
grid=[1,2,3,4]
t=test(grid)
print(grid)
