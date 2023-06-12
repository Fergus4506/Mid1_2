# while True:
#     try:
#         n,p=map(int,input().split())
#         grid=list(map(int,input().split()))
#         think=list(map(int,input().split()))
#         all=0
        


#         # 法1
#         # for x in think:
#         #     all+=x
#         # res=[]
#         # all-=think[0]
#         # for i in range(len(think)):
#         #     max=0
#         #     pos=-1
#         #     for j in range(len(grid)-think[i]+1-all):
#         #         min=grid[j]
#         #         post=j
#         #         for z in range(think[i]-1):
#         #             if grid[j+z+1]<min:
#         #                 min=grid[j+z+1]
#         #             post=j+z+1
#         #         #print(min,max,post)
#         #         if min>max:
#         #             max=min
#         #             pos=post
                
#         #         #print(pos)
#         #     if i+1<len(think):
#         #         all-=think[i+1]
#         #     #print(pos)
#         #     grid=grid[pos+1:]
#         #     #print(*grid)
                    
#         #     res.append(max)
#         # res.sort()
#         # print(res[0])

#     except EOFError:
#         break

#概念對了，但是在確定高度的地方一定要用二分搜尋法來確定才可以，因為搜尋元素一多會導致
#該程式出現TIM的問題
while True:
    try:
        n,p=map(int,input().split())
        grid=list(map(int,input().split()))
        post=list(map(int,input().split()))
        for i in range(len(post)):
            if post[i]==0:
                post[i]=1
        maxN=max(grid)
        while True:
            #print(maxN)
            nowp=0
            pt=0
            check=0
            #第一個for迴圈的目的在於確定是否以現在maxN的高度下是否可以把所有海報成功貼上去
            for i in range(len(grid)):
                if grid[i]>=maxN:
                    nowp+=1
                else:
                    nowp=0
                if nowp==post[pt]:
                    pt+=1
                    nowp=0
                if pt==len(post):
                    check=1
                    break
            #如果可以這裡就會輸出
            if check:
                print(maxN)
                break
            else:
                temp=0
                #循序搜尋下一個高度=>這裡改成二分搜就可以解決(搜尋的時間問題加上py的慢)
                for i in range(len(grid)):
                    if grid[i]<maxN and grid[i]>temp:
                        temp=grid[i]
                if temp==0:
                    print(0)
                    break
                else:
                    maxN=temp
    except EOFError:
        break
