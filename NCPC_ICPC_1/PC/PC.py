# def checkfun(now,checkN,ans,l):
#     if len(checkN)==l:
#         tans=""
#         for i in range(len(ans)):
#             temp=0
#             for j in range(i):
#                 if j<len(checkN) and i-j<len(checkN):
#                     temp+=(int(checkN[j])*int(checkN[i-j]))%10
#             tans=tans+str(temp%10)
#         print(ans,tans,checkN)
#         if tans==ans:
#             return checkN
#         else:
#             return "0"
#     elif now==0:#第一次進入遞迴時只需要考慮到個位數字的次方，因為個位數只有個位數會影響到
#         t=""
#         for i in range(10):
#             if str((i**2)%10)==ans[now]:
#                 t=checkfun(now+1,str(i),ans,l)
#                 if len(t)==l:
#                     return t
#         return -1
#     elif len(checkN)<l:#加數字和驗算的部分
#         print(checkN)
#         for j in range(10):
#             temp=0
#             ckt=str(j)+checkN
#             ck=ckt[::-1]
#             for i in range(now+1):
#                 if i<len(ck) and now-i<len(ck):
#                     temp+=(int(ck[i])*int(ck[now-i]))%10
#                 #print(ck,temp)
#             if str(temp%10)==ans[now]:
#                 t=checkfun(now+1,ckt,ans,l)
#                 # print("@")
#                 # print(t)
#                 if len(t)==l and int(t[0])**2==int(ans[len(ans)-1]):
#                     return t
#         return checkN

def checkfun(checkN,ans,l):
    # print(checkN)
    if len(checkN)==0:
        t=""
        for i in range(0,10):
            temp=(i*i)%10
            if str(temp)==ans[0]:
                t=checkfun(str(i),ans,l)
            if len(t)==l:
                return t
    elif len(checkN)==l:
        # print("@")
        check=1
        for i in range(len(ans)):
            temp=0
            for j in range(i+1):
                if j<len(checkN) and i-j<len(checkN):
                    temp+=(int(checkN[j])*int(checkN[i-j]))%10
            # print(temp%10,end="")
            if str(temp%10)!=ans[i]:
                # print("?")
                check=0
                break
        if check:
            return checkN
        else:
            return ""
    else:
        # print("@")
        for x in range(0,10):
            check=1
            t=checkN+str(x)
            ck=""
            #print(t)
            for i in range(len(t)):
                temp=0
                for j in range(i+1):
                    if j<len(t) and i-j-1<len(t):
                        #print(j,i-j)
                        temp+=(int(t[j])*int(t[i-j]))%10
                #print(temp)
                if str(temp%10)!=ans[i]:
                    check=0
                    break
            #$print()
            if check:
                #print(t,"@")
                ck=checkfun(t,ans,l)
                # print(ck)
            if len(ck)==l:
                return ck
        return ""
        
n=input()
legth=(len(n)+1)//2
In=int(n)
check=0
t=checkfun("",n,legth)
if t==None:
    print(-1)
else:
    print(t)

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


        
