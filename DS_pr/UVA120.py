while True:
    try:
        n=list(map(int,input().split()))
        for i in range(len(n)):
            if i+1==len(n):
                print(n[i])
            else:
                print(n[i],end=" ")
        temp=n[:]
        temp.reverse()
        maxN,minN,endpt=temp[0],temp[0],0
        ans=[]
        for i in temp:
            if  i>maxN:
                maxN=i
        while temp[0]!=maxN or temp[len(temp)-1]!=minN:
            check=False
            mxN=temp.index(maxN)
            if mxN==len(temp)-1:
                mxN=endpt
                endpt+=1
                # print(endpt)
                check=True
            t=temp[mxN:]
            t.reverse()
            ans.append(mxN+1)
            for i in range(len(t)):
                temp[i+mxN]=t[i]
            if check:
                for i in temp[endpt:]:
                    if  i>maxN:
                        maxN=i
            # print(temp)
        ans.append(0)
        for i in range(len(ans)):
            if i+1==len(ans):
                print(ans[i])
            else:
                print(ans[i],end=" ")
       
            
    except EOFError:
        break
