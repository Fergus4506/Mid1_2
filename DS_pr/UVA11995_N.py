while True:
    n=int(input())
    step=[]
    grid=[]
    for i in range(n):
        step.append(list(map(int,input().split())))
    
    maxN=0
    nowst=""
    for i in range(n):
        if step[j][0]==1:  
            grid.append(step[i][1])
            if maxN<step[i][1]:
                maxN=step[i][1]
        elif step[j][0]==2:
            if len(grid)==0 or step[j][1] not in grid:
                print("impossible")
                break
            else:
                pass