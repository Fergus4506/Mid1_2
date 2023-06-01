while True:
    try:
        n=list(input())
        if len(n)==0:
            print()
            continue
        count=0
        for i in range(len(n)):
            if n[i]=="!":
                print()
            elif n[i]=='b':
                for j in range(count):
                    print(" ",end="")
                count=0
            elif ord(n[i])>=ord('0') and ord(n[i])<=ord('9'):
                count+=int(n[i])
            else:
                for j in range(count):
                    print("%s"%(n[i]),end="")
                count=0
        print()
    except EOFError:
        break