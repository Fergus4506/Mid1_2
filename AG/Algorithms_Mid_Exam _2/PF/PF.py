while 1:
    try:
        n=int(input())
        grid1=list(map(int,input().split()))
        grid2=list(map(int,input().split())) 
        grid=[]
        for i in range(n):
            grid.append([grid2[i]/grid1[i],grid1[i],grid2[i]])
        grid.sort(key=lambda x:x[0],reverse=1)
        ans=0
        time=0
        for i in range(n):
            ans+=grid[i][2]*(time+grid[i][1])
            time+=grid[i][1]
        print(ans)
        


    except EOFError:
        break