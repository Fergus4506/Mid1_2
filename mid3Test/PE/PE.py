#盒內塔 但又不適合內塔
#其實盒內塔定義就是把最小的一到次要移動格
#比他大一個的移到主要移動格
#=>所以如果只算移動次數的話連位置都不用管，直接在考慮一層一層的
#移動步數就好了，也就是完滿二元樹的DFS走訪次數
# def Thn(n,move,A,B,C):
#     if(n==1):
#         print("%d 從 %d 移到 %d"%(n,A,C))
#         move+=1
#         return move
#     else:
#         move=Thn(n-1,move,A,C,B)
#         print("%d 從 %d 移到 %d"%(n,A,C))
#         move+=1
#         move=Thn(n-1,move,B,A,C)
#         return move
def hn(n,move):
    if(n==1):
        move+=1
        return move
    else:
        move=hn(n-1,move)
        move+=1
        move=hn(n-1,move)
        return move
while True:
    try:
        m=int(input())
        n=int(input())
        move=0
        # move=Thn(n,0,1,2,3)
        move=hn(n,0)
        print(move*m)
    except EOFError:
        break