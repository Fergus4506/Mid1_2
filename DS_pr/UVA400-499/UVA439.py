
while True:
    try:
        st,ed=input().split()
        f=ord(st[0])
        s=int(st[1])
        ef=ord(ed[0])
        es=int(ed[1])
        BFS=[]
        BFS.append([f,s])
        if st==ed:
            print("To get from %s to %s takes 0 knight moves."%(st,ed))
        else:
            temp=[]
            count=1
            check=0
            while True:
                # print(BFS)
                for i in range(len(BFS)):
                    if  BFS[i][0]-2>=ord('a') and BFS[i][1]-1>=1:
                        temp.append([BFS[i][0]-2,BFS[i][1]-1])

                    if  BFS[i][0]-1>=ord('a') and BFS[i][1]-2>=1:
                        temp.append([BFS[i][0]-1,BFS[i][1]-2])

                    if  BFS[i][0]+1<=ord('h') and BFS[i][1]-2>=1:
                        temp.append([BFS[i][0]+1,BFS[i][1]-2])

                    if  BFS[i][0]+2<=ord('h') and BFS[i][1]-1>=1:
                        temp.append([BFS[i][0]+2,BFS[i][1]-1])

                    if  BFS[i][0]+2<=ord('h') and BFS[i][1]+1<=8:
                        temp.append([BFS[i][0]+2,BFS[i][1]+1])

                    if  BFS[i][0]+1<=ord('h') and BFS[i][1]+2<=8:
                        temp.append([BFS[i][0]+1,BFS[i][1]+2])

                    if  BFS[i][0]-1>=ord('a') and BFS[i][1]+2<=8:
                        temp.append([BFS[i][0]-1,BFS[i][1]+2])

                    if  BFS[i][0]-2>=ord('a') and BFS[i][1]+1<=8:
                        temp.append([BFS[i][0]-2,BFS[i][1]+1])

                for i in range(len(temp)):   
                    if temp[i][0]==ef and temp[i][1]==es:
                        print("To get from %s to %s takes %d knight moves."%(st,ed,count))
                        check=1
                        break
                if check:
                    break
                #print(*temp)
                count+=1
                BFS=temp
                temp=[]
    except EOFError:
        break