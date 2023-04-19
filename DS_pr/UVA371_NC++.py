grid=[]
gridN=[]
def AF(i):
    if i==1:
        return 1
    elif i in grid:
        return gridN[grid.index(i)]+1
    elif i%2:
        count=AF(i*3+1)
        grid.append(i)
        gridN.append(count)
        return count+1
    else:
        count=AF(i//2)
        grid.append(i)
        gridN.append(count)
        return count+1

for i in range(1,5000):
    count=0
    temp=i
    AF(temp)

while True:
    try:
        n=list(map(int,input().split()))
        if n[0]==0 and n[1]==0:
            break
        n.sort()
        maxN,maxNu=0,0
        for i in range(n[0],n[1]+1):
            count=0
            temp=i
            count=AF(temp)-1
            if count>maxNu:
                maxN=i
                maxNu=count
        print("Between %d and %d, %d generates the longest sequence of %d values."%(n[0],n[1],maxN,maxNu))
    except EOFError:
        break

