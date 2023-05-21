while True:
    try:
        n=int(input())
        if n==0:
            break
        grid=[]
        for i in range(n):
            grid.append(list(input()))
        maxN=0
        allX=[]
        for i in range(len(grid)):
            temp=grid[i].count("X")
            allX.append(temp)
            if temp>maxN:
                maxN=temp
        ans=0
        for i in range(len(allX)):
            ans+=maxN-allX[i]
        print(ans)
    except EOFError:
        break