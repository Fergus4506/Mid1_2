while 1:
    try:
        m,n,k=map(int,input().split())
        mGrid=list(map(int,input().split()))
        nGrid=list(map(int,input().split()))
        mGrid.sort()
        nGrid.sort()
        ans=0
        for i in range(m):
            if mGrid[i]>k:
                for j in range(n):
                    if mGrid[i]+nGrid[j]==k:
                        ans+=1
                        break
                    if mGrid[i]+nGrid[j]>k:
                        break
            else:
                for j in range(n-1,-1,-1):
                    if mGrid[i]+nGrid[j]==k:
                        ans+=1
                        break
                    if mGrid[i]+nGrid[j]<k:
                        break
        print(ans)
    except EOFError:
        break