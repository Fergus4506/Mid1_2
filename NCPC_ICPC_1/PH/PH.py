
def main():    
    count=1
    n,m=map(int,input().split())
    grid=[[]for i in range(n)]
    color=0

    #取值，因為是無像圖所以圖形上雙向皆要能通行
    for i in range(m):
        t1,t2=map(int,input().split())
        grid[t1-1].append(t2-1)
        grid[t2-1].append(t1-1)
        color=(color+1)%2

    # print(grid)

    #BFS基礎應用，利用queue將每一個點的子節點算過後在往下走
    #換句話說只要一找到符合條件的點那點就是最短路徑長
    #因為要符合一層一層算的模式所以需要等這層的節點都判斷完後再去更新最大長度和queue的值
    #並且要注意因為這題為無向圖所以不能讓他跑進迴圈中，當判斷到要準備跑到以跑過的節點時就要忽略該資料
    queue=[]
    queue.append(0)
    np=[0 for i in range(n)]#紀錄走過的節點
    ans=1
    while len(queue):
        #print(np)
        zz=queue#該層資料
        for x in range(len(zz)):
            now=zz.pop(0)
            #去抓這層queue中的第一筆資料並去判斷牠的子節點是否符合條件
            for i in range(len(grid[now])):
                if grid[now][i]==n-1:#該子節點為終點，輸出答案並跳出迴圈
                    #print(now)
                    print(ans-1)
                    return None
                elif np[grid[now][i]]:#子節點已走過則忽略(不能將所有走過的點用陣列儲存後再用 in 檢索，因為這樣會超時)
                    continue
                np[grid[now][i]]=1
                queue.append(grid[now][i])
        # print(queue)
        ans+=1
main()

