change=0
def mgSort(grid):
    global change
    if len(grid)==1:
        return grid
    mid=len(grid)//2
    left=mgSort(grid[:mid])
    right=mgSort(grid[mid:])
    # print(left)
    # print(right)
    temp=[]
    while len(left) and len(right):
        if (left[0][0] <= right[0][0]):
            temp.append(left.pop(0))
        else:
            temp.append(right.pop(0))
            change+=len(left)
            

    temp = temp+left if len(left) else temp+right
    # print(temp)
    return temp
        


while 1:
    n=int(input())
    change=0
    if n==0:
        break
    height=list(map(int,input().split()))
    Pclass=input()
    # print(height)
    # print(Pclass)
    grid=[]
    for i in range(n):
        grid.append([height[i],Pclass[i]])
    ans=mgSort(grid)
    print(' '.join(str(x[0]) for x in ans))
    print(''.join(x[1] for x in ans))
    print(change)
    
    
