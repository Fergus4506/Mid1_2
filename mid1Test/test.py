while True:
    try:
        num=list(map(int,input().split()))
        round=list(map(int,input().split()))
        temp=[]
        temp2=[]
        ans=[]
        for s in range(len(num)):   #temp2==num
            temp2.append(num[s]) 

        for i in range(1,len(round)):
            j=round[i]
            while len(temp2)>=j:
                for l in range(j):
                    temp.append(temp2[0])
                    temp2.pop(0)
                temp.reverse()
                for k in range(len(temp)):
                    ans.append(temp[k])
                temp.clear()
            for z in range(len(temp2)):
                ans.append(temp2[0])
                temp2.pop(0)
            for s in range(len(ans)):
                temp2.append(ans[s])
            for x in range(len(num)):
                ans.pop(0)
        for a in range(len(temp2)-1):
            print(temp2[a],end=" ")
        print(temp2[-1])
    except:
        break