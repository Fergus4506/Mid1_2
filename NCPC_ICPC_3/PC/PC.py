#題目要求
#以陣列的形式給予一張無向圖，求符合規則的最長路徑
#規則:當一點要擴展至另一點時要確保下一點的向度比自己多
#    可以從任何一點開始

#分析:
#第一 圖形中的最長路徑=>通常是BFS or DFS=>任何一點都可以=>DFS比較合適
#第二 點最多10**5次方個，單個判斷有可能會導致TLM=>要做"紀錄"的動作
#第三 紀錄=>DP(動態規劃)=>每個點一跑過就要紀錄下來
#第四 紀錄的時機點=>判斷一點是否為最大路經
#     =>經過的點也要記錄他可走的最大路徑
#=>判斷所有的點看哪一個點可以走的距離最長=>就為答案

#注意:無向圖是雙向的，所以在輸入的時候也要幫他反向也設置邊向

#now=>現在判斷的是哪一點
#grid=>無向圖
#maxPass=>原本是用來記錄目前走過的路徑長度，但這樣做的遞迴寫法是錯的
#         更好的作法是讓DFS在回彈時在進行計算會比較好
#allRecheck=>紀錄走過的點
def dfs(now,grid,maxPass,allRecheck):
    # print(now)
    next=grid[now]
    nowmax=maxPass
    for i in range(len(next)):
        temp=0
        #去判斷下一點的向度是否高於目前這一點
        if len(grid[next[i]])>len(next):
            #如果不為0就代表已經走過了，所以直接去拿值就好了
            if allRecheck[next[i]]!=0:
                temp=allRecheck[next[i]]+maxPass
            else:
                #print("@",next[i])
                temp=dfs(next[i],grid,maxPass,allRecheck)+1
                allRecheck[now]=temp
            if temp>nowmax:
                nowmax=temp
    return nowmax

n,m=map(int,input().split())#n為點數 m為邊數

#利用陣列表示無向圖
grid=[[] for i in range(n)]

for i in range(m):
    Index,information=map(int,input().split())

    #要設雙向的邊
    grid[Index].append(information)
    grid[information].append(Index)

#因為n為點數，所以我們可以設立每個點可走最長距離的陣列
#且因為是DFS的關係所以今天記錄下來的值一定是最長路徑(用此也可以判斷該點是否已經走過了)
allRecheck=[0 for i in range(n)]
ans=0
for i in range(len(grid)):
    if allRecheck[i]==0:
        #沒有走過就去使用DFS
        #注意:這裡使用了python在陣列傳值的特性，傳值的時候除非有先做
        #複製的動作不然都會是對同一個，也就是同一指標的陣列做改變
        temp=dfs(i,grid,1,allRecheck)
        allRecheck[i]=temp
    else:
        #有走過就直接去找值就好了
        temp=allRecheck[i]
    if temp>ans:
        ans=temp
print(ans)
