prime=[2,3,5,7,11,13,17,19,23,29,31,37,41]
count=0
def checkDFS(grid,nowSim,ans,last):
    #print(nowSim)
    if(len(grid)==0):
        if (last+1) in prime:
            ans.append(nowSim)
    else:
        for i in range(len(grid)):
            if (last+grid[i]) in prime:
                tempSim=nowSim[:]
                tempSim.append(grid[i])
                tgrid=grid[:]
                tgrid.pop(i)
                checkDFS(tgrid,tempSim,ans,grid[i])
while 1:
    try:
        count+=1
        N=int(input())
        if(count>1):
            print()
        print("Case %d:"%(count))
        grid=[i+1 for i in range(N)]
        grid.pop(0)
        ans=[]
        checkDFS(grid,[1],ans,1)
        # print(ans)
        for i in ans:
            for j in range(len(i)):
                if j==len(i)-1:
                    print(i[j])
                else:
                    print(i[j],end=" ")
    except EOFError:
        break