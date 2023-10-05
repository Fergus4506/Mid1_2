while 1:
    try:
        n=int(input())
        if n==0:
            break
        Sum=0
        grid=[]
        for i in range(n):
            grid.append(float(input()))
            Sum+=grid[-1]
        avg=Sum/n
        lowavg=0
        hiavg=0
        for i in range(n):
            grid[i]=round((grid[i]-avg)*100)/100
            if grid[i]<0:
                lowavg+=grid[i]
            else:
                hiavg+=grid[i]
        if abs(lowavg)<hiavg:
            print("$%.2f"%(abs(lowavg)))
        else:
            print("$%.2f"%(hiavg))

    except EOFError:
        break