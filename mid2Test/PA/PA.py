while True:
    try:
        n=int(input())
        count=1
        if n==0:
            break
        while(n!=1):
            if n%2==0:
                n=n//2
            else:
                n=3*n+1
            count+=1
        print(count)
    except EOFError:
        break