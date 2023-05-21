grid=[]
maxlen=0
while True:
    try:
        temp=list(map(int,input()))
        temp.reverse()
        if len(temp)==1 and temp[0]==0:
            break
        elif len(temp)==0:
            ans=""
            up=0
            for i in range(maxlen):
                t=0
                for j in range(len(grid)):
                    if i<len(grid[j]):
                        t+=grid[j][i]
                        print(grid[j][i],end=" ")
                print()
                up=t//10
                ans=str(t%10)+ans
            print(ans)
            grid=[]
            maxlen=0
        else:
            if len(temp)>maxlen:
                maxlen=len(temp)
            grid.append(temp)
    except EOFError:
        break
ans=""
up=0
for i in range(maxlen):
    t=up
    for j in range(len(grid)):
        if i<len(grid[j]):
            t+=grid[j][i]
    up=t//10
    ans=str(t%10)+ans
if up!=0:
    ans=str(up)+ans
print(ans)