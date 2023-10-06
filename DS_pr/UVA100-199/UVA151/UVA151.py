#最後的點13需減1變成12，再來因為編號從0開始編比較好算，所以真正最後的點會變成11

def Joseph_DP(n,m):
    pos=[0]*n
    pos[0]=0
    for i in range(2,n+1):
        #他是直接去算最後的那個點，pos[i-2]是前一點在人數只有i-1人時的位置，用座標把前面減
        #掉的加回去，然後因為不能超過人數上限所以在%i最後算到i==n人時就代表在人數
        #在題目所給的人數範圍時最後的那一點為誰
        pos[i-1]=(pos[i-2]+m)%i
    return pos[n-1]
while True:
    try:
        n=int(input())
        if n==0:
            break
        m=0
        if n==13:
           m=1
        else:
            m=2
        while(Joseph_DP(n-1,m)!=11):
            m+=1
        print(m)

    except EOFError:
        break
