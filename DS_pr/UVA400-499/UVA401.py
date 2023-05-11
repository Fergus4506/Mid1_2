grid={"A":"A","E":"3","H":"H","I":"I","M":"M","J":"L","L":"J","S":"2","T":"T","U":"U","V":"V","W":"W","X":"X","Y":"Y","8":"8","Z":"5","2":"S","3":"E","5":"Z","1":"1"}
count=0
while True:
    try:
        n=input()
        p=""
        for i in range(len(n)):
            p=n[i]+p
        if p!=n:
            ms=""
            check=0
            for i in range(len(n)):
                if n[i] in grid:
                    ms=grid[n[i]]+ms
                    check+=1
                elif n[i]=="O":
                    check+=1
                    ms=n[i]+ms
                else:
                    ms=n[i]+ms
            if ms==n and check==len(n):
                print("%s -- is a mirrored string."%(n))
            else:
                print("%s -- is not a palindrome."%(n))
        else:
            ms=""
            check=0
            for i in range(len(n)):
                if n[i] in grid:
                    ms=grid[n[i]]+ms
                    check+=1
                elif n[i]=="O":
                    check+=1
                    ms=n[i]+ms
                else:
                    ms=n[i]+ms
            ntemp=""
            for i in range(len(n)):
                if n[i]=="0":
                    ntemp=ntemp+"O"
                else:
                    ntemp=ntemp+n[i]
            #print(ms,ntemp)
            if ms==ntemp and check==len(n):
                print("%s -- is a mirrored palindrome."%(n))
            else:
                print("%s -- is a regular palindrome."%(n))
        print()
    except EOFError:
        break