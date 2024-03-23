while 1:
    A,B=map(int,input().split())
    if A==0 and B==0:
        break
    A_list=list(map(int,input().split()))
    B_list=list(map(int,input().split()))
    A_list.sort()
    B_list.sort()
    A_list=set(A_list)
    B_list=set(B_list)
    same=len(A_list&B_list)
    print(min(len(A_list),len(B_list))-same)
