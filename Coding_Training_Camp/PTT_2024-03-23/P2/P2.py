n=int(input())
for i in range(n):
    temp=input()
    le=len(temp)
    x=int(temp)
    check=1
    for j in range(x//2,x):
        # print(j,sum([int(k) for k in str(j)])+j)
        if x==sum([int(k) for k in str(j)])+j:
            print(j)
            check=0
            break
    if check:
        print(0)
