import math
while True:
    try:
        M,N=map(int,input().split())
        K=int(input())
        count=0
        if K<M or K>N:
            print("-1")
            continue
        while M<=N:
            count+=1
            temp=(M+N)//2
            if temp==K:
                break
            if K>temp:
                M=temp+1
            else:
                N=temp-1
            # print(M,N)
        print(count)
    except EOFError:
        break