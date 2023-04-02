while True:
    try:
        n=input().split()
        noIn=list(map(int,input().split()))
        data=n[0].split("/")
        grid=[]
        for i in range(int(n[1])):
            grid.append(i+1)
        visited=[]
        last=0
        now=int(data[0])
        first=int(data[0])
        ans=0
        count=0
        check=0
        cker=False
        for i in range(8):
            while now in noIn or now in visited or now>int(n[1]):
                if now==first and check:
                    now=last+1
                    if now>int(n[1]):
                        now-=int(n[1])
                    first=now
                    check=0
                    continue
                elif now in noIn:
                    last=now
                    now+=10
                    ans+=1
                elif now in visited:
                    last=now
                    now+=10
                if now>int(n[1]):
                    now-=int(n[1])
                # print(now)
                count+=1
                # if count==100:
                #     cker=True
                #     break
                check=1
            # if cker:
            #     break
            visited.append(now)
            last=now
            now+=10
            # print(visited)
        for i in range(8):
            if i+1==8:
                print(visited[i])
            else:
                print(visited[i],end=" ")
        print("Li's angry number is %d"%(ans))
    except EOFError:
        break
            
