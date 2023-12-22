n=int(input())
for i in range(n):
    x=int(input())
    ans=""
    # print(x//-2,x%-2)
    if x==0:
        print("Case #%d: %s"%(i+1,0))
    else:
        count=-1
        while x!=0:
            if x==1:
                ans="1"+ans
                x=0
            elif x>0:
                ans=str(x%2)+ans
                x=-(x//2)
            else:
                ans=str(abs(x)%2)+ans
                x=abs(x)//2+1
        print("Case #%d: %s"%(i+1,ans))
