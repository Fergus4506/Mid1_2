n=int(input())
for i in range(n):
    maxL=0
    mxGird=[]
    for j in range(10):
        temp=input().split()
        if int(temp[1])>maxL:
            mxGird=[]
            mxGird.append(temp[0])
            maxL=int(temp[1])
        elif int(temp[1])==maxL:
            mxGird.append(temp[0])
    print("Case #%d:"%(i+1))
    for j in mxGird:
        print(j)
