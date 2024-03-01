while 1:
    try:
        s=input().split(" ")
        s.sort()
        double=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=="x2":
                double+=1
            else:
                break
        if double!=0:
            s=list(map(int,s[:-double]))
        else:
            s=list(map(int,s))
        ans,last,count=0,s[0],1
        for i in range(1,len(s)):
            if last==s[i]:
                count+=1
                if double and count%2==0:
                    ans+=last*2
                    double-=1
                if count%3==0:
                    ans+=last
            else:
                last=s[i]
                count=1
        print(ans)


    except EOFError:
        break