def find_power_of_two(num):
    power=0
    while num>1:
        num=num/2
        power+=1
    return power
while True:
    try:
        n,k=map(int,input().split())
        field=[[1,1],[1,2],[2,2],[2,1]]
        if n==1:
            print(field[k-1])
        else:
            subn=4
            p=subn//2
            disp=n//4
            cp=subn
            subn//4
            dis=[]
            count=n-1
            while count!=3:
                for i in range(disp):
                    dis.append(count)
                count-=2
            dis.append(3)
            dis.append(1)
            dis.append(1)
            dis.append(3)
            if n>4:
                redis=dis[:]
                redis.reverse()
                dis+=redis
            for l in range(find_power_of_two(n)-1):
                t=field[:]
                for i in range(4):
                    if i==0:
                        for j in range(0,(subn//2)2):
                            t[j].reverse()
                    elif i==1:
                        for j in range((subn//2)2,(subn//2)**22): 
                            t[j][1]+=p
                    elif i==2:
                        for j in range((subn//2)2*2,(subn//2)23):
                            t[j][0]+=p
                            t[j][1]+=p
                    else:
                        temp2=[]
                        temp2=t[:cp]
                        temp2.reverse()
                        for j in range(len(temp2)):
                            temp2[j][0]+=dis[j]
                            t.append(temp2[j])
                field=t[:]
                subn=2
                p=subn//2
                cp=subn
                subn//4
            print(t)
            print(field[k-1])
    except EOFError:
        break