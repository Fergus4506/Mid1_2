count=0
while True:
    n=list(map(int,input().split()))
    if not count:
        count=1
        print("PERFECTION OUTPUT")
    check=0
    for i in n:
        if i==0:
            check=1
            break
        cha=0
        for j in range(1,i):
            if i%j==0:
                cha+=j
                #print(j)
            if cha>i:
                print("{:5d}  ABUNDANT".format(i))
                break
        if cha==i:
            print("{:5d}  PERFECT".format(i))
        elif cha<i:
            print("{:5d}  DEFICIENT".format(i))



    if check:
        print("END OF OUTPUT")
        break
    #111