#dp基礎題
#利用不斷去更新目前陣列的最大總和來去和所有總和中最大值去做比較
#ex:4 12 -17 5 8 -2 7 -3
#在跑到 -17 前 curr和rus都是16，但到-17時就只有curr會更新到-1而rus則是維持16
#而跑到5後因為前面的-1不要去管的話5自己本身還比較大所以會將curr更新到5，以此類推就會是整個演算法的過程


while 1:
    try:
        n=int(input())
        grid=list(map(int,input().split()))
        curr,rus=grid[0],grid[0]
        for i in range(1,n):
            curr=max(curr+grid[i],grid[i])
            if curr>rus:
                rus=curr
        if rus<0:
            print(0)
        else:
            print(rus)
    except EOFError:
        break