while True:
    n=int(input())
    if n==0:
        break
    ans=0
    for i in range(n,0,-1):
        ans=ans+i*i
    print(ans)
    
