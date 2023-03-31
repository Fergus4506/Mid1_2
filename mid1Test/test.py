grid=[]
ans=[]

def chk(k,now,temp,need,pl):
    
    if pl>=k:
        return None

    if now>=k:
        t=0
        for i in need:
            t+=i    
        if t not in ans:
            ans.append(t)
    else:
        chk(k,now+1,temp,need,pl)
        for i in range(pl,len(temp)):
            pl=now+i
            need[now]=temp[pl]
            pu=need[:]
            chk(k,now+1,temp,pu,pl)

temp=list(map(int,input().split()))
n=temp[0]
k=temp[1]
temp=list(map(int,input().split()))
need=temp[:k]
chk(k,0,temp,need,k)
ans.sort()
a=0
for i in range(2,ans[len(ans)-1]+1):
    check=True
    for j in range(2,int(i**0.5)):
        if i%j==0:
            check=False
            break
    if check:
        grid.append(i)
for i in ans:
    if i in grid:
        a+=1
print(a)