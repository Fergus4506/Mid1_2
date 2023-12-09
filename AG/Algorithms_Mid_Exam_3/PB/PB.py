def DFScheck(grid,now,ans,al,dis):
    if len(now)==al:
        if (now[len(now)-1]+1) in dis:
            ans.append(now)
        # print(ans)
    else:
        for i in range(len(grid)):
            if now[len(now)-1]+grid[i] in dis:
                temp=grid[:]
                temp.pop(i)
                t=now[:]
                t.append(grid[i])
                DFScheck(temp,t,ans,al,dis)
count=0
while 1:
    try:
        count+=1
        n=int(input())
        grid=[i+1 for i in range(n)]
        grid.pop(0)
        dis=[2]
        for i in range(3,100,2):
            ck=1
            for j in range(2,(int)(i**0.5)+1):
                if i%j==0:
                    ck=0
                    break
            if ck:
                dis.append(i)
        ans=[]
        # print(dis)
        DFScheck(grid,[1],ans,n,dis)
        # print(ans)
        print("Case %d:"%(count))
        for i in ans:
            print(*i)
    except EOFError:
        break