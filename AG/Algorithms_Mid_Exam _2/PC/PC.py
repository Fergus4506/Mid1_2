while 1:
    try:
        n,m=map(int,input().split())
        grid=[[1 for i in range(m)] for j in range(n)]
        grid[0][0]=0
        ans=0
        
    except EOFError:
        break