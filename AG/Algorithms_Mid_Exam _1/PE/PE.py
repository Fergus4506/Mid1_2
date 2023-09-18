n=int(input())
for i in range(n):
    howMuch=int(input())
    grid=list(map(int,input().split()))
    grid.sort()
    ans=0
    buf=howMuch
    for i in range(howMuch):
        ans+=grid[i]*buf
        buf-=1
    print(ans)