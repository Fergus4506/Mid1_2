n=int(input())
for x in range(n):
    bk=input()
    itemN=int(input())
    maxCt=int(input())
    grid=[]
    for i in range(itemN):
        grid.append(int(input()))
    grid.sort(reverse=1)
    # print(grid)
    ans=0
    ckl=[grid[0]]
    for i in range(1,len(grid)):
        ck=1
        for j in range(len(ckl)):
            if ckl[j]+grid[i]<=maxCt:
                ans+=1
                ckl.pop(j)
                ck=0
                break
        if ck:
            ckl.append(grid[i])
    print(ans+len(ckl))
    if x!=n-1:
        print()