while True:
    try:
        n=int(input())
        max=0
        deep=1
        check=0
        back=0
        for i in range(n):
            temp=list(map(int,input().split()))
            if temp[0]==0 and temp[1]==0:
                if deep>max:
                    max=deep
                if back:
                    deep-=1
                else:
                    if check:
                        deep-=1
                        check=0
                        back=1
                    else:
                        check=1
            else:
                deep+=1
                check=0
                if back==1:
                    back=0
            #print(deep)
        if deep>max:
            max=deep
        print(max)


    except EOFError:
        break