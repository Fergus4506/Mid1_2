while 1:
    try:
        x=int(input())
        list_a=list(map(int,input().split()))
        list_a.reverse()
        ans=list_a[1]
        for i in range(2,len(list_a)):
            ans+=list_a[i]*(i)*(x**(i-1))
        print(ans)
    except EOFError:
        break
