def printS(s):
    for i in range(len(s)):
        print(s[i],end="")
def chToStr(s):
    temp=""
    for i in range(len(s)):
        temp+=s[i]
    return temp
while True:
    try:
        n=list(input())
        fir=n[0]
        if n.count(fir)==len(n):
            printS(n)
            print()
            continue
        pr=n
        temp=""
        alpr=[]
        printS(pr)
        alpr.append(chToStr(pr))
        for i in range(1,len(n)):
            temp=pr[0]
            pr=pr[1:]
            pr.append(temp)
            st=chToStr(pr)
            if st not in alpr:
                print(" ",end="")
                printS(pr)
                alpr.append(st)
        print()
    except EOFError:
        break