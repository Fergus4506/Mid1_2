while True:
    try:
        t=input().split()
        step=t[1]
        grid=list(map(int,input().split()))
        for i in range(len(step)):
            last=-1
            zgrid=0
            if step[i]=="R":
                for j in range(len(grid)-1,-1,-1):
                    now=grid.pop()
                    if last==now:
                        last=last*2
                        grid.insert(0,last)
                        zgrid+=1
                        last=-1
                    elif now==0:
                        zgrid+=1
                    else:
                        if last==-1:
                            last=now
                        else:
                            grid.insert(0,last)
                            last=now
                    #print(grid)
                if last!=-1:
                    grid.insert(0,last)
                
                for j in range(zgrid):
                    grid.insert(0,0)      
                # print(grid)
            else:
                for j in range(len(grid)):
                    now=grid.pop(0)
                    if last==now:
                        last=last*2
                        grid.append(last)
                        zgrid+=1
                        last=-1
                    elif now==0:
                        zgrid+=1
                    else:
                        if last==-1:
                            last=now
                        else:
                            grid.append(last)
                            last=now
                    # print(grid)
                if last!=-1:
                    grid.append(last)
                
                for j in range(zgrid):
                    grid.append(0)      
                # print(grid)
        for i in range(len(grid)):
            if i+1==len(grid):
                print(grid[i])
            else:
                print(grid[i],end=" ")

    except EOFError:
        break