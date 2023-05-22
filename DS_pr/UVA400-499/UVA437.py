count=1
#題目為動態規劃，顧名思義就是利用前面已做過的資料去判斷後續資料的變化為何
#此題利用LIS來解題，LIS為最長遞增子字串的簡稱，利用前面算好的子字串長度去判斷接下來的方塊
#要去拿哪一個已堆積好總高度才會符合最大高度
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
    inputB.sort(key=lambda x:x[1])
    inputB.sort(key=lambda x:x[0])
    LIS=[]
    # print(inputB)
    for i in range(len(inputB)):
        LIS.append(inputB[i][2])
        for j in range(i):
            if inputB[i][0]>inputB[j][0] and  inputB[i][1]>inputB[j][1] and LIS[j]+inputB[i][2]>LIS[i]:
                LIS[i]=LIS[j]+inputB[i][2]
        # for i in range(len(LIS)):
        #     print(LIS[i])
    print("Case %d: maximum height = %d"%(count,max(LIS)))
    count+=1