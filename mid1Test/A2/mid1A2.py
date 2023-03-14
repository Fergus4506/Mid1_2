while True:
    try:
        n=list(map(int,input().split()))
        step=list(map(int,input().split()))
        temp=[0]*len(n)
        for i in range(1,len(step)):
            for j in range(0,len(n),step[i]):
                if j+step[i]>len(n):
                    break
                for z in range(step[i]):
                    temp[j+step[i]-z-1]=n[j+z]
                for z in range(step[i]):
                    n[j+z]=temp[j+z]
        for i in range(len(n)):
            if i==0:
                print(n[i],end="")
            else:
                print(" %d"%(n[i]),end="")
        print()
    except:
        break