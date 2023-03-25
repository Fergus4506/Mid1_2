n=int(input())
grid=[[i+1]for i in range(n)]
now=[]*n
while True:
    t=input().split()
    tg=int(t[1])
    ds=int(t[3])
    print(grid)
    if t[0]=="quit":
        break
    if t[0]=="move":
        if t[3]=="onto":#元素上
            pass
        elif t[3]=="over":#整個陣列上
            grid[ds-1].append(tg)
            rm=grid[now[tg-1]].index(tg)
            grid[now[int(t[1])-1]].pop(rm)
            now[int(t[1])-1]=int(t[3])
    elif t[0]=="pile":
        if t[3]=="onto":
            pass
        elif t[3]=="over":
            pass
