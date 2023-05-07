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
while True:
    try:
        n,p=map(int,input().split())
        grid=list(map(int,input().split()))
        post=list(map(int,input().split()))
        maxN=max(grid)
        while True:
            #print(maxN)
            nowp=0
            pt=0
            check=0
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
            if check:
                print(maxN)
                break
            else:
                temp=0
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
