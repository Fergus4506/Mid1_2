while True:
    try:
        n=list(map(int,input().split()))
        for i in n:
            r,l,w=1,1,1
            ck=True
            for j in range(i-1):
                if l==1:
                    if ck:
                        r+=1
                        ck=False
                    else:
                        w=0
                        l+=1
                        r-=1
                        ck=True
                elif r==1:
                    if ck:
                        l+=1
                        ck=False
                    else:
                        w=1
                        l-=1
                        r+=1
                        ck=True
                else:
                    if w:
                        r+=1
                        l-=1
                    else:
                        r-=1
                        l+=1
            print("TERM %d IS %d/%d"%(i,l,r))
    except EOFError:
        print()
        break