while True:
    try:
        n=list(map(int,input().split()))
        temp=n[:]
        temp.reverse()
        maxN,minN=temp[0],temp[0]
        ans=[]
        for i in temp:
            if  i>maxN:
                maxN=i
            if i<minN:
                minN=i
        for i in range(len(n)-1):
            if temp[0]==maxN and temp[len(temp)-1]==minN:
                break
            t=temp[i:]
            t.reverse()
            for j in range(len(t)):
                temp[j+i]=t[j]
            
    except EOFError:
        break