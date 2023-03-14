List=list(input())
ICP={"(":4,"*":2,"/":2,"+":1,"-":1,")":0}
ISP={"*":2,"/":2,"+":1,"-":1,")":0,"(":0}
ans=[]
temp=[]
for i in range(len(List)):
    if List[i]=="(":
        temp.append("(")
    elif List[i]==")":
        while temp[len(temp)-1]!="(":
            ans.append(temp.pop())
        temp.pop()
    elif List[i]=="*" or List[i]=="/" or List[i]=="+" or List[i]=="-":
        if len(temp)==0:
            temp.append(List[i])
        elif ICP[List[i]]>ISP[temp[len(temp)-1]]:
            temp.append(List[i])
        else:
            ans.append(temp.pop())
            while ICP[List[i]]<=ISP[temp[len(temp)-1]]:
                ans.append(temp.pop())
                if len(temp)==0:
                    break
            temp.append(List[i])
    else:
        ans.append(List[i])
for i in range(len(temp)):
    ans.append(temp.pop())

for i in range(len(ans)):
    if i==len(ans)-1:
        print(ans[i])
        break
    print(ans[i],end=" ")

temp=[] 
for i in range(len(ans)):
    if ans[i]=="*":
        b=int(temp.pop())
        a=int(temp.pop())
        temp.append(str(a*b))
        for j in range(len(temp)):
            print(temp[j],end=" ")
        for j in range(i+1,len(ans)):
            if j==len(ans)-1:
                print(ans[j])
                break
            print(ans[j],end=" ")
    elif ans[i]=="/":
        b=int(temp.pop())
        a=int(temp.pop())
        temp.append(str(int(a/b)))
        for j in range(len(temp)):
            print(temp[j],end=" ")
        for j in range(i+1,len(ans)):
            if j==len(ans)-1:
                print(ans[j])
                break
            print(ans[j],end=" ")
    elif ans[i]=="+":
        b=int(temp.pop())
        a=int(temp.pop())
        temp.append(str(a+b))
        for j in range(len(temp)):
            print(temp[j],end=" ")
        for j in range(i+1,len(ans)):
            if j==len(ans)-1:
                print(ans[j])
                break
            print(ans[j],end=" ")
    elif ans[i]=="-":
        b=int(temp.pop())
        a=int(temp.pop())
        temp.append(str(a-b))
        for j in range(len(temp)):
            print(temp[j],end=" ")
        for j in range(i+1,len(ans)):
            if j==len(ans)-1:
                print(ans[j])
                break
            print(ans[j],end=" ")
    else:
        temp.append(ans[i])

