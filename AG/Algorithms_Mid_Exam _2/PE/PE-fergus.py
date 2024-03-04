while 1:
    try:
        temp=input()
        n=list(map(int,temp[1:-1].split(',')))
        # print(n)
        ans=[]
        ans.append(n[0])
        ans.append(n[1])
        ans.append(n[2])
        for i in range(3,len(n)):
            tempSum=[]
            
            for j in range(i-3+1):
                tempSum.append(ans[j]+n[i])
            ans.append(max(tempSum))
        print(ans)
        print(max(ans))
    except EOFError:
        break