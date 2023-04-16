#DFS的應用法，確定目前這個位置訪問過後再去尋找四周其他位置的點是否符合需求，
#如果符合的話往下一個點前進，並在該點重複執行上述動作，如果四周皆跑完的話
#則返回上一層繼續檢查上層還未檢查完成的點

def ckwar(grid,isVs,nowY,nowX):

    #這些點皆為不可跑到的點(EX:不存在grid上、已走訪過...)
    if nowX<0 or nowX==len(grid):
        return 
    elif nowY<0 or nowY==len(grid):
        return
    elif grid[nowY][nowX]!="1" or isVs[nowY][nowX]==1:
        return
    
    #設定已走訪過
    isVs[nowY][nowX]=1

    #四周八點
    dir=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

    #跑遞迴走訪四周八點
    for i in range(8):
        ckwar(grid,isVs,nowY+dir[i][0],nowX+dir[i][1])

count=1
while True:
    try:
        n=int(input())
        grid=[]
        for i in range(n):
            grid.append(input())
        isVs=[[0]*n for i in range(n)]
        #print(isVs)

        ans=0
        for i in range(n):
            for j in range(n):
                if grid[i][j]=="1" and isVs[i][j]!=1:#如果該點未走訪過且點符合題目需求
                    ckwar(grid,isVs,i,j)
                    ans+=1


        print("Image number %d contains %d war eagles."%(count,ans))
        count+=1
    except EOFError:
        break