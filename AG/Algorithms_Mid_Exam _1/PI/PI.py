count=0
while 1:
    count+=1
    n,limit=map(int,input().split())
    k=n
    if n==-1 and limit==-1:
        break
    cnt=1
    while n!=1:
        if n>limit:
            cnt-=1
            break
        if n%2:
            n=3*n+1
        else:
            n=n//2
        cnt+=1
    print("Case %d: K = %d, limit = %d, number of terms = %d"%(count,k,limit,cnt))