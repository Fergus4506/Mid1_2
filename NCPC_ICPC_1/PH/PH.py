def main():    
    n,m=map(int,input().split())
    grid=[[]for i in range(n)]
    color=0

    #取值，因為是無像圖所以圖形上雙向皆要能通行
    for i in range(m):
        t=list(map(int,input().split()))
        grid[t[0]-1].append(t[1]-1)
        grid[t[1]-1].append(t[0]-1)
        color=(color+1)%2

    # print(grid)

    #BFS基礎應用，利用queue將每一個點的子節點算過後在往下走
    #換句話說只要一找到符合條件的點那點就是最短路徑長
    #因為要符合一層一層算的模式所以需要等這層的節點都判斷完後再去更新最大長度和queue的值
    #並且要注意因為這題為無向圖所以不能讓他跑進迴圈中，當判斷到要準備跑到以跑過的節點時就要忽略該資料
    queue=[]
    queue.append(0)
    np=[]
    ans=1
    check=0
    while len(queue):
        zz=queue
        for x in range(len(zz)):
            now=zz.pop(0)
            for i in range(len(grid[now])):
                if grid[now][i] in np:
                    continue
                elif grid[now][i]==n-1:
                    # print(now)
                    print(ans-1)
                    check=1
                    break
                np.append(grid[now][i])
                queue.append(grid[now][i])
            if check:
                break
        ans+=1
        if check:
            break
main()