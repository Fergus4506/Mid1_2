grid=[]
grid.append(1)
grid.append(2)
for i in range(3,2001,2):
    check=1
    for j in range(3,int(i**0.5)+1,2):
        if i%j==0:
            check=0
            break
    if check:
        grid.append(i)
#print(*grid)
count=0
while True:
    try:
        n,c=map(int,input().split())
        if count:
            print()
        print("%d %d: "%(n,c),end="")
        index=0
        for i in range(len(grid)):
            if grid[i]>n:
                index=i
                break
            elif grid[i]==n:
                index=i+1
                break
        temp=grid[:index]
        if len(temp)%2==0:
            if c*2>=len(temp):
                print(*temp)
            else:
                f=(len(temp)-c*2)//2
                e=f+c*2
                pt=temp[f:e]
                print(*pt)
        else:
            if c*2-1>=len(temp):
                print(*temp)
            else:
                f=(len(temp)-(c*2-1))//2
                e=f+(c*2-1)
                pt=temp[f:e]
                print(*pt)
        count=1
    except EOFError:
        print()
        break