#霍夫曼樹實作
#霍夫曼樹就類似一種加密的手段，利用建立好的密碼表來解碼或是編碼
#所以要實作霍夫曼樹就要實作出三種功能
#分別是建立密碼表、解碼和編碼

#建立密碼表的部分，題目給的霍夫曼樹都會符合完整二元樹的特性，
#所以可以利用判斷高度的數學式子反推後得知他的父節點位置
#就可以得到類似走訪的功能
def crht(grid):
    count=0
    ans=[]
    for i in range(len(grid)):
        count=(i+1)//2
        if grid[i]!="0":
            temp=i+1
            pt=""
            while temp!=1:
                if temp%2==0:
                    pt="0"+pt
                else:
                    pt="1"+pt
                    temp-=1
                temp=temp//2
            ans.append([grid[i],pt])
            print(ans)
    return ans

#編碼的部分
#編碼的部分比較簡單，因為只需找尋對應英文字母的對應密碼值
#再將全部接再一起就好了
def encode(case,grid):
    # print(grid)
    ans=""
    for i in range(len(case)):
        for j in range(len(grid)):
            if case[i]==grid[j][0]:
                ans=ans+grid[j][1]
                break
    return ans

#編碼的部分
#編碼需要去考慮長度的問題
#所以去確認密碼時要先從最長的密碼值開始確認
#當確認出現在的密碼可以符合前面的區段時
#把密碼所代表的值抓出來、修改接下來要確定的密碼值，
# 並且跳出最內圈的迴圈使程式重複從最長的密碼判斷
def decode(case,grid):
    temp=case[:]
    ans=""
    while len(temp)!=0:
        for i in range(len(grid)-1,-1,-1):
            if len(grid[i][1])<=len(temp):
                t="".join(temp[:len(grid[i][1])])
                if t==grid[i][1]:
                    ans=ans+grid[i][0]
                    temp=temp[len(grid[i][1]):]
                    break
        # print(*temp)
    return ans
                



while True:
    try:
        tree=input().split()
        incodeForm=crht(tree)
        n=int(input())
        for i in range(n):
            case=input()
            if case.isdigit():
                print(decode(case,incodeForm))
            else:
                pass
                print(encode(case,incodeForm))
    except EOFError:
        break