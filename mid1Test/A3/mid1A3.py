while True:
    n=int(input())
    if n==0:
        break
    temp=list(map(int,input().split()))
    ans=0
    group=n//2
    temp.sort()
    for i in range(group):
        if i+1==group:
            print(temp[i]+temp[n-i-1])
        else:
            print(temp[i]+temp[n-i-1],end=" ")
    
    