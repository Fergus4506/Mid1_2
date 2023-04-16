dir=[1,5,10,25,50]
grid=[0]*30001
grid[0]=1
#DP 動態規劃->簡單說就是利用存較小的值來換算較大的值
#這題概念-> 假設現在要找10->10單一一枚,
#5+5->5+5,5+1*5[這項是假設其中一個五是固定不能改變的(也就是最後進來的)，而剩下的錢可以有什麼變化，變化的部分可以由前面算過的數字得知]
#所以5+5這項有兩種可能，且能拆分成多少可以從5的那一項中得知
#而最後一種則是全為1 所以為4種方法。

#總結:先算小的就可以從小的慢慢得知大的數所存在的種類，這部分的應用就是DP的實現，

for i in dir:
    for j in range(i,30001):
        grid[j]+=grid[j-i]#固定一枚硬幣後往前找去抓剩下硬幣可能的變化種數


while True:
    try:
        n=int(input())
        if grid[n]==1 or n==0:
            print("There is only 1 way to produce %d cents change."%(n))
        else:
            print("There are %d ways to produce %d cents change."%(grid[n],n))
    except EOFError:
        break