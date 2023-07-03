def checkfun(now,checkN,ans):
    if now==len(ans)+1:
        return True
    temp=0
    for i in range(now):
        if i<len(checkN) and now-i-1<len(checkN):
            temp+=(int(checkN[i])*int(checkN[now-i-1]))%10
    #print(temp)
    if str(temp%10)==ans[len(ans)-now]:
        #print("@")
        return checkfun(now+1,checkN,ans)
    else:
        #print("@@")
        return False
n=input()
if len(n)%2==0:
    print(-1)
else:
    legth=(len(n)+1)//2
    In=int(n)
    start=1
    end=9
    check=1
    for i in range(legth-1):
        start=start*10
    if start!=1:
        start=start+1
    for i in range(legth-1):
        end=end*10+9
    for i in range(start,(end+1)//2):
        if checkfun(1,str(i)[::-1],n):
            print(i)
            check=0
            break
        #print("")
    if check:
        print(-1)

        
