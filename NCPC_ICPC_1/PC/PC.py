n=input()
if len(n)%2==0:
    print(-1)
else:
    legth=(len(n)+1)//2
    In=int(n)
    start=1
    end=9
    for i in range(legth-1):
        start=start*10
    if start!=1:
        start=start+1
    for i in range(legth-1):
        end=end*10+9
    for i in range(start,end+1):
        t=str(i)
        a=0
        ans=[]
        for j in range(len(n)):
            ans.append(0)
        for j in range(len(t)):
            for z in range(len(t)):
                ans[z+j]+=int(t[z])*int(t[j])
        for j in range(len(ans)):
            a=a*10+int(ans[j])%10
        if a==In:
            print(i)
            break
        
