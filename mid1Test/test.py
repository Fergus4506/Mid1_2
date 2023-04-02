# grid=[]
# ans=[]

# def chk(k,now,temp,need,pl):
    
#     if pl>=k:
#         return None

#     if now>=k:
#         t=0
#         for i in need:
#             t+=i    
#         if t not in ans:
#             ans.append(t)
#     else:
#         chk(k,now+1,temp,need,pl)
#         for i in range(pl,len(temp)):
#             pl=now+i
#             need[now]=temp[pl]
#             pu=need[:]
#             chk(k,now+1,temp,pu,pl)

# temp=list(map(int,input().split()))
# n=temp[0]
# k=temp[1]
# temp=list(map(int,input().split()))
# need=temp[:k]
# chk(k,0,temp,need,k)
# ans.sort()
# a=0
# for i in range(2,ans[len(ans)-1]+1):
#     check=True
#     for j in range(2,int(i**0.5)):
#         if i%j==0:
#             check=False
#             break
#     if check:
#         grid.append(i)
# for i in ans:
#     if i in grid:
#         a+=1
# print(a)
while 1:
    try:
        n,ppl=input().split()
        day,month=map(int,n.split("/"))
        ppl=int(ppl)
        absent=list(map(int,input().split()))
        att=[]
        std=[]
        last=0
        repeat=day
        add=day%10
        current=day
        status=-1
        jjz=0

        while len(att)<8:
            if current>ppl:
                if add==0:
                    current=10
                else:
                    current=add
            while current in std:
                if current>ppl:
                    if add==0:
                        current=10
                    else:
                        current=add
                current=last+1
                add=(add+1)%10
            if current in absent:
                jjz+=1
            else:
                att.append(current)
            std.append(current)
            last=current
            current+=10

        print(*att)
        print("Li's angry number is %d"%jjz)    
    except EOFError:
        break