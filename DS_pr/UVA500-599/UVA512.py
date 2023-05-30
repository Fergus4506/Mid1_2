count=1
while True:
    try:
        error=0
        check=0
        if count>1:
            b=input()
            if b=="0 0":
                break
            elif b=="":
                r,c=map(int,input().split())
                check=1
            else:
                r,c=map(int,b.split())
                check=1
        else:
            r,c=map(int,input().split())
        if r==0 and c==0:
            break
        elif check:
            print()
        print("Spreadsheet #%d"%(count))
        grid=[]
        for i in range(r):
            temp=[]
            for j in range(c):
                t=str(i+1)+" "+str(j+1)
                temp.append(t)
            grid.append(temp)
        n=int(input())
        for i in range(n):
            com=input().split()
            #print(*com)
            if com[0]=="DR":
                ct=0
                for j in range(int(com[1])):
                    grid.pop(int(com[j+2])-1-ct)
                    ct+=1
                    r-=1
            elif com[0]=="DC":
                ct=0
                for j in range(int(com[1])-1,-1,-1):
                    for z in range(len(grid)):
                        grid[z].pop(int(com[j+2])-1)
            elif com[0]=="IR":
                ct=0
                for j in range(int(com[1])):
                    t=["-1"]*len(grid[0])
                    grid.insert(int(com[j+2])-1+ct,t)
                    ct+=1
            elif com[0]=="IC":
                ct=0
                for j in range(int(com[1])):
                    for z in range(len(grid)):
                        grid[z].insert(int(com[j+2])-1+ct,"-1")
                    ct+=1
            elif com[0]=="EX":
                grid[int(com[1])-1][int(com[2])-1],grid[int(com[3])-1][int(com[4])-1]=grid[int(com[3])-1][int(com[4])-1],grid[int(com[1])-1][int(com[2])-1]           
        if error:
            break
        n2=int(input())
        for i in range(n2):
            y,x=map(int,input().split())
            t=str(y)+" "+str(x)
            check=1
            for j in range(len(grid)):
                if t in grid[j]:
                    where=grid[j].index(t)
                    print("Cell data in (%d,%d) moved to (%d,%d)"%(y,x,j+1,where+1))
                    check=0
                    break
            if check:
                print("Cell data in (%d,%d) GONE"%(y,x))
        count+=1
    except EOFError:
        break