count=1
while True:
    n=int(input())
    if n==0:
        break
    inputB=[]
    for i in range(n): 
        tx,ty,tz=map(int,input().split())
        inputB.append([tx,ty,tz])
        inputB.append([tx,tz,ty])
        inputB.append([ty,tx,tz])
        inputB.append([ty,tz,tx])
        inputB.append([tz,ty,tx])
        inputB.append([tz,tx,ty])
    inputB.sort(key=lambda x:x[1],reverse=1)
    inputB.sort(key=lambda x:x[0],reverse=1)
    LIS=[]
    print(inputB)
    for i in range(len(inputB)):
        if i==0:
            for j in range(len(inputB)):
                LIS.append([inputB[i]])
        else:
            for j in range(i):
                if inputB[i][0]<LIS[j][len(LIS[j])-1][0] and  inputB[i][1]<LIS[j][len(LIS[j])-1][1]:
                    LIS[j].append(inputB[i])
        for i in range(len(LIS)):
            print(LIS[i])
    ans=[]
    for i in range(len(LIS)):
        temp=0
        for j in range(len(LIS[i])):
            temp+=LIS[i][j][2]
        ans.append(temp)
    print("Case %d: maximum height = %d"%(count,max(ans)))
    count+=1

