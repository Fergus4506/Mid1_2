while True:
    n=int(input())
    step=[]
    grid=[]
    for i in range(n):
        step.append(list(map(int,input().split())))
    
    maxN=0
    dt={1:"stack",2:"queue",3:"priority queue",4:"not sure"}
    last=0
    lastS=0
    for i in range(n):
        if step[i][0]==1:  
            grid.append(step[i][1])
            if maxN<step[i][1]:
                maxN=step[i][1]
        elif step[i][0]==2:
            if len(grid)==0 or step[i][1] not in grid:
                print("impossible")
                break
            else:
                now=grid.index(step[i][1])
                tl=0
                tls=0
                if step[i][1]==maxN:
                    if now==0:
                        tl=4
                        tls=2
                    elif now==len(grid)-1:
                        tl=4
                        tls=1
                    else:
                        tl=3
                else:
                    if now==0:
                        tl=2
                    elif now==len(grid)-1:
                        tl=1
                if 