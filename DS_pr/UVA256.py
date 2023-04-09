while True:
    try:
        n=int(input())
        ans=[]
        for i in range(10**(n//2)):
            temp1=i**2
            temp2=temp1//10**(n//2)+temp1%10**(n//2)
            if temp2==i:
                ans.append(temp1)
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