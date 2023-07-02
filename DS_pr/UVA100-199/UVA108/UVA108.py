n=int(input())
count=0
grid=[[]for i in range(n)]
allGrid=[]
check=0
while True:
    try:
        if check==n**2:
            break
        t=list(map(int,input().split()))
        for j in range(len(t)):
            if count==n:
                count=0
            grid[count].append(t[j])
            count+=1
            check+=1
    except EOFError:
        break
if n==1:
    print(grid[0][0])
else:
    maxR=grid[0][0]
    for z in range(n):
        tempar=[0]*n
        for i in range(z,n):
            for j in range(n):
                tempar[j]+=grid[i][j]
                #print(temp)
                #print(tempar)
            tempMax=tempar[0]
            countMax=tempar[0]
            for k in range(len(tempar)):
                countMax+=tempar[k]
                tempMax=max(countMax,tempMax)
                countMax=max(0,countMax)
            maxR=max(tempMax,maxR)
    print(maxR)

#以下為GPT的解釋範例輸出:
#該程式是利用給的二維陣列一定是正方形來做特殊的計算
#先將0-1 0-2 0-3 0-4...分別存入一個一維陣列中，該陣列代表目前這一行
#從頭到尾的加總，然後再用Kadane去尋找這一行矩陣中最大的連續子序列
#最後利用max去判段最大子字串有沒有大於目前加總的最大值
        #allGrid.append(tempar)
        #print(allGrid)
    # for z in range(len(allGrid[0])):
    #     for i in range(n):
    #         temp=0
    #         for j in range(i,n):
    #             temp+=allGrid[j][z]
    #             if temp>maxR:
    #                 maxR=temp
    # print(maxR)

#n = int(input())
# grid = [list(map(int, input().split())) for _ in range(n)]

# if n == 1:
#     print(grid[0][0])
# else:
#     max_sum = float('-inf')
#     for i in range(n):
#         row_sums = [0] * n
#         for j in range(i, n):
#             for k in range(n):
#                 row_sums[k] += grid[j][k]
#                 print(row_sums)
#             max_row_sum = max_ending_here = 0
#             for k in range(n):
#                 max_ending_here = max(0, max_ending_here + row_sums[k])
#                 max_row_sum = max(max_row_sum, max_ending_here)
#             max_sum = max(max_sum, max_row_sum)
#             print(max_sum)
#             print(row_sums)
#     print(max_sum)
            

