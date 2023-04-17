#想規律不要硬炸
while True:
    try:
        n=list(map(int,input().split()))
        for i in n:
            temp=i
            count,ckL=1,0
            while True:
                if temp-count<=0:
                    ckL=count
                    break
                temp-=count
                count+=1
            #print(ckL)
            #print(temp)
            if ckL%2==0:
                print("TERM %d IS %d/%d"%(i,1+temp-1,ckL-temp+1))
            else:
                print("TERM %d IS %d/%d"%(i,ckL-temp+1,1+temp-1))

    except EOFError:
        break