n=int(input())
grid=[1,2]
for i in range(3,30001,2):
    check=1
    for j in range(3,int(i**0.5)+1):
        if i%j==0:
            check=0
            break
    if check:
        grid.append(i)
print(grid)
ans=[1,1]
for i in range(n):
    s,e=map(int,input().split())
    for j in range(s,e+1):
        if j in grid:
            continue
        elif j==1:
            continue
        else:
            temp=j
            # print(j)
            count=0
            now=0
            while temp>=grid[now]:
                if temp%grid[now]==0:
                    count+=1
                now+=1
            if count>ans[1]:
                ans=[j,count]
    print(ans)