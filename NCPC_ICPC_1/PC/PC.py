# def checkfun(now,checkN,ans):
#     if now==len(ans)+1:
#         return True
#     temp=0
#     for i in range(now):
#         if i<len(checkN) and now-i-1<len(checkN):
#             temp+=(int(checkN[i])*int(checkN[now-i-1]))%10
#     #print(temp)
#     if str(temp%10)==ans[len(ans)-now]:
#         #print("@")
#         return checkfun(now+1,checkN,ans)
#     else:
#         #print("@@")
#         return False

check=0

def checkfun(now,checkN,ans,l):
    if now==len(ans):
        global check
        check=1
        return checkN
    elif now==0:#第一次進入遞迴時只需要考慮到個位數字的次方，因為個位數只有個位數會影響到
        t=""
        for i in range(10):
            if str((i**2)%10)==ans[now]:
                t=checkfun(now+1,str(i),ans,l)
                if len(t)==l:
                    return t
        return -1
    elif len(checkN)<l:#加數字和驗算的部分
        # print(checkN)
        for j in range(10):
            temp=0
            ckt=str(j)+checkN
            ck=ckt[::-1]
            for i in range(now+1):
                if i<len(ck) and now-i<len(ck):
                    temp+=(int(ck[i])*int(ck[now-i]))%10
                #print(ck,temp)
            if str(temp%10)==ans[now]:
                t=checkfun(now+1,ckt,ans,l)
                # print("@")
                # print(t)
                if len(t)==l and int(t[0])**2==int(ans[len(ans)-1]):
                    return t
        return checkN
    else:#不用加數字了，但須去確認後面的是否符合乘法成出來的答案
        temp=0
        ck=checkN[::-1]
        for i in range(now+1):
            if i<len(checkN) and now-i<len(checkN):
                # print(i,now-i)
                temp+=(int(ck[i])*int(ck[now-i]))%10
            #print(checkN,temp,now)
        if str(temp%10)==ans[now]:
            t=checkfun(now+1,checkN,ans,l)
            # print(t)
            if len(t)==l and int(t[0])**2==int(ans[len(ans)-1]) and check:
                return t
        return "0"

inp=input()
n=inp[::-1]
if len(n)%2==0:
    print(-1)
else:
    legth=(len(n)+1)//2
    In=int(n)
    check=0
    print(checkfun(0,"",n,legth))

    # start=1
    # end=9
    # check=1
    # for i in range(legth-1):
    #     start=start*10
    # if start!=1:
    #     start=start+1
    # for i in range(legth-1):
    #     end=end*10+9
    # for i in range(start,(end+1)//2):
    #     if checkfun(1,str(i)[::-1],n):
    #         print(i)
    #         check=0
    #         break
    #     #print("")
    # if check:
    #     print(-1)


        
