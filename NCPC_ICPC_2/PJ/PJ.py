#題目需求:
#這是一個遊戲，給定一個序列，要求玩家按照順序相加平均後找出最大值
#特殊規則:可以喊一次暫停和一次開始，這樣是為了讓玩家可以去省略某部分的數字
#ex:
#1 2 3 -4 5 6
#可以在算完3的時候喊暫停，忽略-4後再喊開始，這樣就會讓加總變為1+2+3+5+6

#解題重點:
#以 1 2 3 -4 5 6 為例，這裡可以很明顯看出可以分為三塊
#前面的 1 2 3 / 忽略的 -4 / 後面的 5 6
#但是 前面的 1 2 3 再加上後面的 5 6 算平均後並不會比 5+6/2 的平均來的大
#所以真正要算的其實就是前面往後抓會出現比較大的還是經過分割後面的那塊會比較大

#ex:
#1. 1 2 3 -4 3 2 1
#這種可能區分後抓前面抓後面都沒差，選一個輸出就好了

#2. 1 2 3 -4 5 6
#這樣區分後比起抓 1+2+3+5+6/5 來說 5+6/2 比較大，所以會抓後面的來當作答案
#換句話說就是還沒到5之前都是被省略的

#3. 5 6 -4 -3 -5 -2 
#同上面的概念，只是比較不一樣的是算完6後面的全部都被省略了

#注意:
#1.
#要怎麼做出這樣的分區相加呢
#=>前綴總和prefix sum 後綴總和 suffix sum
#前綴總和=>就是普通的相加而已
#後綴總和=>簡單來說就是從最後一個元素慢慢加回到最前面而已
#2.
#如果算出來都是負數的話要記得輸出0=>全部忽略



n=int(input())
grid=list(map(int,input().split()))

#先計算加總的值並用一個變數存著避免重複計算導致TLM
gridsum=sum(grid)

#記錄現在計算的值是多少
prenow=grid[0]
sufnow=gridsum

#在計算的時候就去動態的更新最大值
premax=grid[0]
sufmax=gridsum/len(grid)


for i in range(1,n):

    #因為後綴總和在程式中的算法是先從全部都已經算到的部分開始慢慢減少相加的元素
    #故使用-=
    sufnow-=grid[i-1]
    prenow+=grid[i]
    if prenow/(i+1)>premax:
        premax=prenow/(i+1)
    if sufnow/(n-i)>sufmax:
        sufmax=sufnow/(n-i)
    # print(premax,sufmax)
# print(prefix)

#裡面有if ... > 0是為了避免負數的問題
if premax>sufmax:
    if premax>0:
        print("%.9f"%(premax))
    else:
        print("%.9f"%(0))
else:
    if sufmax>0:
        print("%.9f"%(sufmax))
    else:
        print("%.9f"%(0))
        