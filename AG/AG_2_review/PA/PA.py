n=int(input())
for i in range(n):
    x=int(input())
    count=0
    ans=0
    while x!=0:
        if count%2:
            ans+=x%1000
        else:
            ans-=x%1000
        x=x//1000
        count+=1
    if ans%13==0:
        print(abs(ans),"YES")
    else:
        print(abs(ans),"NO")