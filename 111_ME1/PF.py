count=0
while True:
    try:
        n=int(input())
        count+=1
        dit={0:"",1:"hundred",2:"thousand",3:"million",4:"billion",5:"trillion"}
        much={0:1,1:10**2,2:10**3,3:10**6,4:10**9,5:10**12}
        ans=""
        if n==0:
            print("Case %d: %s"%(count,0))
            continue
        for i in range(5,-1,-1):
            if i>1:
                # print(i)
                temp=""
                for j in range(1,-1,-1):
                    now=much[j]*much[i]
                    # print(now)
                    # print(n)
                    if n//now!=0:
                        if j==0:
                            temp=temp+str(n//now)+" "
                        else:
                            temp=temp+str(n//now)+" "+dit[j]+" "
                        n=n%now
                if temp!="":
                    ans=ans+temp+dit[i]+" "
            else:
                if i==1:
                    now=much[i]
                    if n//now!=0:
                        ans=ans+str(n//now)+" "+dit[i]+" "
                        n=n%now
                else:
                    now=1
                    if n//now!=0:
                        ans=ans+str(n//now)+" "+dit[i]+" "
        ans.strip()
        print("Case %d: %s"%(count,ans))
    except EOFError:
        break