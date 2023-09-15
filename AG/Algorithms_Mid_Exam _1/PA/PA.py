change=0
def mgSort(grid):
    global change
    if len(grid)==1:
        return grid
    mid=len(grid)//2
    left=mgSort(grid[:mid])
    right=mgSort(grid[mid:])
    temp=left+right
    print(temp)

    #切割合併後sort的迴圈(取最小值放到最前面)
    for i in range(len(temp)):
        nowMin=temp[i][0]
        Minpos=i
        for j in range(i+1,len(temp)):
            if temp[j][0]<nowMin:
                Minpos=j
                nowMin=temp[j][0]
        if i!=Minpos:
            change+=1
            temp[i],temp[Minpos]=temp[Minpos],temp[i]
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
    
    
