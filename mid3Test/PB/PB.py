ct=1
while 1:
    try:
        n,lim=map(int,input().split())
        if n==-1 and lim==-1:
            break
        temp=n
        count=1
        while temp!=1:
            if temp%2:
                temp=temp*3+1
            else:
                temp=temp//2
            
            if temp>lim:
                break
            count+=1
        print("Case %d: K = %d, limit = %d, number of terms = %d"%(ct,n,lim,count))
        ct+=1
    except EOFError:
        break