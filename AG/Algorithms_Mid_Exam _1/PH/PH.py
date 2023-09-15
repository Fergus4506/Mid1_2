#dp基礎題
#題目:
# 小朋友玩上樓梯遊戲，每一步可以往上走一階或兩階，開始位置在第0階，從第1階開始每
# 階都有一個數字，踩在第i階，分數就要扣第i階的數字，請問走到第n階的最少扣分是多少。

#假設我今天要走到第五階，我就要去知道第四階和第三階分別會扣幾分，以此類推，走到第三和四就要分別知道 1 2 和 2 3
#這種越拆越小的方式就是DP的實作模式

while 1:
    try:
        n=int(input())
        grid=list(map(int,input().split()))
        ans=[0]*n
        ans[0]=grid[0]
        ans[1]=grid[1]
        for i in range(2,n):
            t=min(ans[i-2],ans[i-1])
            ans[i]=grid[i]+t
        print(ans[len(ans)-1])
    except EOFError:
        break