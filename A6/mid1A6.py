ans=["1"]
while True:
    n=int(input())
    if n==-1:
        break
    if n+1<=len(ans):
        print(ans[n])
    else:
        for i in range(len(ans),n+1):
            read=list(map(int,ans[i-1]))
            countN=0
            count=0
            ansS=""
            for j in range(len(read)):
                if j==0:
                    countN=read[0]
                    count+=1
                else:
                    if countN!=read[j]:
                        ansS=ansS+str(count)+str(countN)
                        countN=read[j]
                        count=1
                    else:
                        count+=1
            ansS=ansS+str(count)+str(countN)
            ans.append(ansS)
        print(ans[n])
