while True:
    try:
        temp=list(map(int,input().split()))
        maxN,minN=temp[0],temp[0]
        nc=0
        for i in range(len(temp)):
            if i+1==len(temp):
                print(temp[i])
            else:
                print(temp[i],end=" ")
            if temp[i]>maxN:
                maxN=temp[i]
            if temp[i]<minN:
                minN=temp[i]  
        alMax=maxN      
        temp.reverse()
        ans=[]
        while temp[0]!=alMax or temp[len(temp)-1]!=minN:
            if temp[len(temp)-1]==maxN:
                t=temp[nc:]
                t.reverse()
                for i in range(len(t)):
                    temp[i+nc]=t[i]
                ans.append(nc+1)
                nc+=1
                maxN=temp[nc]
                for i in range(nc,len(temp)):
                    if temp[i]>maxN:
                        maxN=temp[i]
            else: 
                now=temp.index(maxN)
                t=temp[now:]
                ans.append(now+1)
                t.reverse()
                for i in range(len(t)):
                    temp[i+now]=t[i]
        ans.append(0)
        for i in range(len(ans)):
            if i+1==len(ans):
                print(ans[i])
            else:
                print(ans[i],end=" ")
            
    except EOFError:
        break