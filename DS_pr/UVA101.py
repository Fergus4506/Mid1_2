n=int(input())
grid=[[i]for i in range(n)]
now=[]
for i in range(n):
    now.append(i)
while True:
    t=input().split()
    if t[0]=="quit":
        for i in range(n):
            if len(grid[i])==0:
                print("%d: "%(i))
            else:
                print("%d:"%(i),end="")
                for j in range(len(grid[i])):
                    print(" %d"%(grid[i][j]),end="")
                print()
        break
    tg=int(t[1])
    ds=int(t[3])
    if t[0]=="move":
        if t[2]=="onto":#元素上
            if now[ds]==tg:
                inpt=grid[ds].index(ds)
                grid[ds].insert(inpt+1,tg)
                rm=grid[now[tg]].index(tg)
                grid[now[tg]].pop(rm)
                now[tg]=ds
            else:
                inpt=grid[now[ds]].index(ds)
                grid[now[ds]].insert(inpt+1,tg)
                rm=grid[now[tg]].index(tg)
                grid[now[tg]].pop(rm)
                now[tg]=now[ds]
        elif t[2]=="over":#整個陣列上
            if now[ds]==tg:
                grid[ds].append(tg)
                rm=grid[now[tg]].index(tg)
                grid[now[tg]].pop(rm)
                now[tg]=ds
            else:
                grid[now[ds]].append(tg)
                rm=grid[now[tg]].index(tg)
                grid[now[tg]].pop(rm)
                now[tg]=now[ds]
    elif t[0]=="pile":
        if t[2]=="onto":
            pt=grid[now[tg]].index(tg)
            temp=grid[now[tg]][pt:]
            inpt=grid[now[ds]].index(ds)
            for i in temp:
                grid[now[tg]].remove(i)
                grid[now[ds]].insert(inpt+1,i)
                inpt+=1
                if i!=tg:
                    now[i]=now[ds]
            now[tg]=now[ds]
        elif t[2]=="over":
            pt=grid[now[tg]].index(tg)
            temp=grid[now[tg]][pt:]
            for i in temp:
                grid[now[tg]].remove(i)
                grid[now[ds]].append(i)
                if i!=tg:
                    now[i]=now[ds]
            now[tg]=now[ds]
    print(grid)