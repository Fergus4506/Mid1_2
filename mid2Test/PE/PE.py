while True:
    try:
        n=input()
        le=len(n)
        count=0
        for i in range(1,le+1):
            if le%i==0:
                temp=[]
                t=""
                for j in range(le):
                    if j%i==0 and j!=0:
                        temp.append(t)
                        t=n[j]
                    else:
                        t=t+n[j]
                temp.append(t)
                temp.sort()
                t=""
                for j in range(le//i):
                    t=t+temp[j]
                if t!=n:
                    print(t)
                    count=1
        if count==0:
            print("orz")
    except EOFError:
        break