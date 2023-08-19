import math
#題目需求，給你很多的果醬和不確定數量但知道能放多少果醬的箱子
#求一個箱子內可以放置最多的果醬數量能使每個箱子放置的果醬數量較平均

#解題過程:
#知道箱子能放多少果醬的話可以從中得知需要多少箱子=>box=(果醬數量//能放多少)=>多出來的果醬放不滿一個箱子
# =>最少要用box+1個箱子=>知道要用幾個箱子後再去除果醬數量就是答案了


n,m=map(int,input().split())
start=2
ans=1
if n<=m:
    print(n)
else:
    howMuchBox=math.ceil(n/m)
    print(n//howMuchBox)