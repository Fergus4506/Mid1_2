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
            pass
        elif t[2]=="over":#整個陣列上
            pass
    elif t[0]=="pile":
        if t[2]=="onto":
            pass
        elif t[2]=="over":
            pass