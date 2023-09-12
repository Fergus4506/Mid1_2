max=0
endPoint=0

def DFSpass(Record,now,grid,length):
    global max,endPoint
    lastpoint=grid[now]
    # print(Record,length)
    for i in range(len(lastpoint)):
        if lastpoint[i] in Record:
            continue
        nowRecord=Record[:]
        nowRecord.append(lastpoint[i])
        DFSpass(nowRecord,lastpoint[i],grid,length+1)
    # print(length)
    if length>max or (length==max and endPoint>now):
        max=length
        endPoint=now
count=0
while 1:
    max=0
    endPoint=0
    count+=1
    n=int(input())
    if n==0:
        break
    s=int(input())
    grid=[[]for i in range(n)]
    while 1:
        point=list(map(int,input().split()))
        if point[0]==point[1]:
            break
        grid[point[0]-1].append(point[1]-1)
    # print(grid)
    DFSpass([s-1],s-1,grid,0)
    if max:
        print("Case %d: The longest path from %d has length %d, finishing at %d."%(count,s,max,endPoint+1))
    else:
        print("Case %d: The longest path from %d has length %d, finishing at %d."%(count,s,max,s))
    print()
    
