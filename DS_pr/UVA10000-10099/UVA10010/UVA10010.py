Cs=int(input())
def next_part(code,grid,now):
    if code==1:
        now[0]-=1
        now[1]-=1
    elif code==2:
        now[0]-=1
    elif code==3:
        now[0]-=1
        now[1]+=1
    elif code==4:
        now[1]-=1
    elif code==5:
        now[1]+=1
    elif code==6:
        now[0]+=1
        now[1]-=1
    elif code==7:
        now[0]+=1
    elif code==8:
        now[0]+=1
        now[1]+=1
    if (now[0]<len(grid) and now[0]>-1) and (now[1]>-1 and now[1]<len(grid[0])):
        # print(grid[now[0]][now[1]])
        return now
    else:
        return [-1,-1]

def checkStr(target,grid,now):
    # print(target)
    if len(target)==1:
        return 1
    code=[]
    print(now)
    # print(grid)
    if now[0]-1>-1:
        if now[1]-1>-1:
            if target[1]==grid[now[0]-1][now[1]-1]:
                code.append(1)
        if target[1]==grid[now[0]-1][now[1]]:
            code.append(2)
        if now[1]+1<len(grid[0]):
            if target[1]==grid[now[0]-1][now[1]+1]:
                code.append(3)
    if now[1]-1>-1:
        if target[1]==grid[now[0]][now[1]-1]:
            code.append(4)
    if now[1]+1<len(grid[0]):
        if target[1]==grid[now[0]][now[1]+1]:
            code.append(5)
    if now[0]+1<len(grid):
        if now[1]-1>-1:
            if target[1]==grid[now[0]+1][now[1]-1]:
                code.append(6)
        if target[1]==grid[now[0]+1][now[1]]:
            code.append(7)
        if now[1]+1<len(grid[0]):
            if target[1]==grid[now[0]+1][now[1]+1]:
                code.append(8)

    print(code)
    if len(code):
        for x in code:
            cd=x
            # print(x)
            tpnow=now[:]
            count=1
            ck=[]
            kk=1
            for i in range(1,len(target)):
                count+=1
                tpnow=next_part(cd,grid,tpnow)
                # print(grid[tpnow[0]][tpnow[1]],tpnow[0],tpnow[1])
                if tpnow[0]==-1 and tpnow[1]==-1:
                    # print("@")
                    kk=0
                    break
                elif grid[tpnow[0]][tpnow[1]]!=target[i]:
                    # print(tpnow[0],tpnow[1])
                    kk=0
                    break
                ck.append(grid[tpnow[0]][tpnow[1]])

        # print(target[1:],ck)       
        if len(target)==count:
            # print("U")
            return 1
        else:
            return 0
    else:
        return 0

        
for i in range(Cs):
    if Cs>1:
        blank=input()
        if i>0:
            print()
    y,x=map(int,input().split())
    grid=[]
    gridS=[[] for j in range(x)]
    # print(gridS)
    for j in range(y):
        grid.append(list(input().lower()))
    needToCheck=int(input())
    for j in range(needToCheck):
        t=list(input().lower())
        for a in range(y):
            check=0
            for b in range(x):
                if t[0]==grid[a][b]:
                    if checkStr(t,grid,[a,b]):
                        print(a+1,b+1)
                        check=1
                        break
                    else:
                        # print("@")
                        # print()
                        pass
            if check:
                break

    