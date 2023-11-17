def checkDFS(grid,gn,check,cn,ans,nowSim):
    # print(gn,cn)
    if gn==len(grid) or cn==len(check):
        # print("@")
        ans.append(nowSim)
        return -1
    else:
        for i in range(cn,len(check)):
            tempSim=nowSim
            if(grid[gn]==check[i]):
                tempSim+=check[i]
                checkDFS(grid,gn+1,check,i+1,ans,tempSim)
        checkDFS(grid,gn+1,check,cn,ans,nowSim)
while 1:
    try:
        n1=input()
        n2=input()
        ans=[]
        output=[]
        if(len(n1)>=len(n2)):
            checkDFS(n2,0,n1,0,ans,"")
        else:
            checkDFS(n1,0,n2,0,ans,"")
        maxlen=0
        for i in ans:
            if len(i)>maxlen:
                maxlen=len(i)
        for i in ans:
            if len(i)==maxlen and i not in output:
                output.append(i)
        print("\n".join(sorted(output)))
    except EOFError:
        break