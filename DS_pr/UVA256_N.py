while True:
    try:
        n=int(input())
        ans=[]
        for i in range(10**n):
            if int(i**0.5)**2!=i:
                continue
            else:
                temp=i//(10**(n//2))+i%(10**(n//2))
                # print(temp)
                temp=temp**2
                if temp==i:
                    ans.append(temp)
        for i in ans:
            if n==2:
                print("{:02d}".format(i))
            elif n==4:
                print("{:04d}".format(i))
            elif n==6:
                print("{:06d}".format(i))
            elif n==8:
                print("{:08d}".format(i))
        
    except EOFError:
        break