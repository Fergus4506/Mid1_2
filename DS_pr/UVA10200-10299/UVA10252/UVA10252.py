while 1:
    try:
        s1=input()
        s2=input()
        for i in range(26):
            now=chr(i+ord('a'))
            t1=s1.count(now)
            t2=s2.count(now)
            t=min(t1,t2)
            if t!=0:
                for j in range(t):
                    print(now,end="")
        print()

    except EOFError:
        break