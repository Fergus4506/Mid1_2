while 1:
    try:
        grid=list(map(int,input().split()))
        tg=int(input())
        cnt=0
        l,r=0,len(grid)-1
        while 1:
            # print(l,r)
            now=(l+r)//2
            if grid[now]==tg:
                print(cnt)
                break
            elif l>=r:
                print(-1)
                break
            elif grid[now]>tg:
                r=now-1
            else:
                l=now+1
            cnt+=1
    except EOFError:
        break