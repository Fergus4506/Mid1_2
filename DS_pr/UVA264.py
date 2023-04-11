grid=[[1,1,1,1]]
while True:
    try:
        n=list(map(int,input().split()))
        for i in n:
            if len(grid)>=i:
                print("TERM %d IS %d/%d"%(i,grid[i-1][0],grid[i-1][1]))
            else:
                l,r,w=grid[len(grid)-1][0],grid[len(grid)-1][1],grid[len(grid)-1][2]
                ck=grid[len(grid)-1][3]
                for j in range(i-len(grid)):
                    if l==1:
                        if ck:
                            r+=1
                            ck=False
                        else:
                            r-=1
                            l+=1
                            w=0
                            ck=True
                    elif r==1:
                        if ck:
                            l+=1
                            ck=False
                        else:
                            l-=1
                            r+=1
                            w=1
                            ck=True
                    else:
                        if w:
                            r+=1
                            l-=1
                        else:
                            r-=1
                            l+=1
                    #print("%d %d"%(l,r))
                    grid.append([l,r,w,ck])
                print("TERM %d IS %d/%d"%(i,l,r))

    except EOFError:
        break