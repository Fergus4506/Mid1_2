def l(index,res,grid):
    if res==None:
        res=[]
    if (index)>=len(grid):
        return res
    if grid[index]=="None":
        return res
    res.append(grid[index])
    res=l((index+1)*2-1,res,grid)
    res=l((index+1)*2,res,grid)
    return res
    
while True:
    try:
        grid=input().split()
        res=[]
        ans=[]
        total=0
        for x in grid:
            if x!="None":
                total+=int(x)
        for i in range(1,len(grid)):
            res.append(sum(list(map(int,(l(i,None,grid))))))
        for i in res:
            ans.append((total-i)*i)
        
        print(max(ans))
                
        
        
    except EOFError:
        break