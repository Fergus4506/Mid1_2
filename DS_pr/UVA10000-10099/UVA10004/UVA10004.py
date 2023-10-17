#題目概要
#給你一個圖形，去判斷該點和周圍的點所填的顏色是否不同
#解題概念:用DFS去把每個點都塗上顏色，每過一個點就跟換一種顏色，共兩種顏色
#如果今天點已經塗好顏色了則去判斷顏色是否符合現在的需求，不符合則要回傳0
#把每一點都跑完後如果符合規則則回傳1


# def BFSpass(grid,start):
#     queue=[[start]]
#     while len(queue):
#         now=queue.pop(0)
#         nextNode=grid[now[-1]]
#         for i in range(len(nextNode)):
#             if nextNode[i] in now:
#                 return 0
#             else:
#                 t=nextNode[:]
#                 t.append(nextNode[i])
#                 queue.append(t)
#     return 1
#概念是對的，因為要有環路的出現才會有鄰近的顏色填一樣的可能性存在
#但是如果環路是偶數也就是1->2->3->4->1的情況下還是符合條件的，所以整體上BFS還是錯的

def DFSpass(now,grid,color,paint):
    # print(now)
    now_color=(color+1)%2

    #已經塗好顏色的點代表已走訪過，不需用走訪第二次，只需要確認是否符合規則就好
    if paint[now]==-1:#未塗色的點要先塗色
        paint[now]=now_color
    elif paint[now]!=now_color:#不符合規則
        return 0
    elif paint[now]==now_color:#符合規則
        return 1
    
    #塗好這個點後再去找下面的點，確認是否需要塗顏色或是符不符合規則
    for i in range(len(grid[now])):
        if not DFSpass(grid[now][i],grid,now_color,paint):
            return 0
    return 1
#DFSpass(0,grid,0,paint)    
    
while 1:
    try:
        n=int(input())
        if n==0:
            break
        L=int(input())
        grid=[[]for i in range(n)]
        for i in range(L):
            temp=list(map(int,input().split()))
            grid[temp[0]].append(temp[1])
            #grid[temp[1]].append(temp[0])
        paint=[-1 for i in range(n)]
        if DFSpass(0,grid,0,paint) :
            print("BICOLORABLE.")
        else:
            print("NOT BICOLORABLE.")
        
    except EOFError:
        break
    