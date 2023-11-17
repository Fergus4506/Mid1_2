prime=[2,3,5,7,11,13,17,19,23,29,31,37,41]
count=0
def checkDFS(grid,nowSim,ans,last):
    #print(nowSim)
    if(len(grid)==0):
        if nowSim not in ans and (last+1) in prime:
            ans.append(nowSim)
    else:
        for i in range(len(grid)):
            if (last+grid[i]) in prime:
                tempSim=nowSim
                tempSim+=str(grid[i])
                tgrid=grid[:]
                tgrid.pop(i)
                checkDFS(tgrid,tempSim,ans,grid[i])
while 1:
    try:
        count+=1
        print("Case %d:"%(count))
        N=int(input())
        grid=[i+1 for i in range(N)]
        grid.pop(0)
        ans=[]
        checkDFS(grid,"1",ans,1)
        for i in ans:
            print(" ".join(i))
    except EOFError:
        break