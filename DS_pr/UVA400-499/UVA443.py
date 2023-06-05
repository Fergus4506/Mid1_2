#BFS應用題 算出一陣列，陣列中的元素均只以2 3 5 7為因數的數字
#Ex:28=2*2*7 30=2*3*5
#這種要算多種可能性的題目=>利用BFS就可以算出=>要去使用到queue

grid=[1]
queue=[1]
prime=[2,3,5,7]
while len(queue)!=0:
    check=0
    checkNum=queue.pop(0)
    for i in range(4):
        temp=checkNum*prime[i]
        
        #這裡是用題目的範例測試資料推出來的，我們可以知道當數字到達2000000000時
        #就可以不用在考慮比該數字更大的範圍了，也就是說不須用在queue中添加更多
        #種可能性去計算，只需將queue剩下的值全部並判斷是否可以加入陣列中即可
        if temp>2000000000:
            break
        else:
            if grid.count(temp)==0:
                grid.append(temp)
                queue.append(temp)
grid.sort()
while True:
    try:
        n=int(input())
        if n==0:
            break
        if n%100!=11 and n%10==1:
            print("The %dst humble number is %d."%(n,grid[n-1]))
        elif n%100!=12 and n%10==2:
            print("The %dnd humble number is %d."%(n,grid[n-1]))
        elif n%100!=13 and n%10==3:
            print("The %drd humble number is %d."%(n,grid[n-1]))
        else:
            print("The %dth humble number is %d."%(n,grid[n-1]))
        
    except EOFError:
        break