#此題目標在於找到一個中間點令所有數字可以區分為兩堆且兩堆數字總和會相同

#因為要去區分大小堆所以要利用排序後數列的特性從兩端慢慢相加
#但今天是因為測資設計的關係可以直接用sort就可以完成排序(quick sort)不會炸
#不然應該自己寫sort出來會比較保險
n=int(input())
allAnimal=[]
for i in range(n):
    allAnimal.append(int(input()))
allAnimal.sort()

#這裡的目的就是為找到中間點的程式
#須注意一點，有可能算到一半左右相加就相等了
#這時候需要重製目前正在計算的左右相加值並且從目前右側+1 and 左側-1的位置來繼續做
minN,maxN=allAnimal[0],allAnimal[len(allAnimal)-1]#左右目前的相加值
left,right=0,len(allAnimal)-1#左側和右側目前跑到哪裡了
ansleft,ansright=0,0#相等後記錄目前相等的位置在哪裡
while left<right:
    if maxN>minN:#目前右側較大，所以左側加數字並往後推一個
        left+=1
        minN+=allAnimal[left]
    elif minN>maxN:#目前左側較大，所以右側加數字並往前推一個
        right-=1
        maxN+=allAnimal[right]
    if minN==maxN:#相等的資料更新
        ansleft=left
        ansright=right
        left,right=left+1,right-1
        maxN=allAnimal[right]
        minN=allAnimal[left]
    
#print(allAnimal[ansleft:ansright])

#因為題目有說到一定可以找一點使兩數可以分堆，所以不用考慮有很多動物無法分堆的問題
#只有可能會出現一隻動物無法分堆使那隻動物變為中間點
if ansleft+1==ansright:
    if allAnimal[ansleft]==allAnimal[ansright]:#左右最後一個分堆的點一樣，因為無法區分兩點所以以該點為分界
        print(allAnimal[ansleft])
    else:#點已經全部用完了，所以區分點抓最小的就是左側最後一點+1
        print(allAnimal[ansleft]+1)
else:#還有一點沒有使用的情況
    print(allAnimal[ansleft+1])