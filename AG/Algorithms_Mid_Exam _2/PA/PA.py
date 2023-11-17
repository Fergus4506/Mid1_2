while 1:
    try:
        m,n,k=map(int,input().split())
        mGrid=list(map(int,input().split()))
        nGrid=list(map(int,input().split()))
        mGrid.sort()
        nGrid.sort()
        ans=0
        ms=0
        ns=n-1
        while 1:
            if mGrid[ms]+nGrid[ns]==k:
                ans+=1
                ms+=1
                ns-=1
            elif mGrid[ms]+nGrid[ns]>k:
                ns-=1
            elif mGrid[ms]+nGrid[ns]<k:
                ms+=1
            if ms==m or ns<0:
                break
        print(ans)
    except EOFError:
        break