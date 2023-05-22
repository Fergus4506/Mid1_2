def main():
    while True:
        try:
            st,ed=input().split()
            BFS=[]
            BFS.append(st)
            if st==ed:
                print("To get from %s to %s takes 0 knight moves."%(st,ed))
            else:
                temp=[]
                count=1
                while True:
                    for i in range(len(BFS)):
                        if  ord(BFS[i][0])-2>=ord('a') and int(BFS[i][1])-1>=1:
                            s=str(chr(ord(BFS[i][0])-2))+str(int(BFS[i][1])-1)
                            temp.append(s)
                        if  ord(BFS[i][0])-1>=ord('a') and int(BFS[i][1])-2>=1:
                            s=str(chr(ord(BFS[i][0])-1))+str(int(BFS[i][1])-2)
                            temp.append(s)
                        if  ord(BFS[i][0])+1<=ord('h') and int(BFS[i][1])-2>=1:
                            s=str(chr(ord(BFS[i][0])+1))+str(int(BFS[i][1])-2)
                            temp.append(s)
                        if  ord(BFS[i][0])+2<=ord('h') and int(BFS[i][1])-1>=1:
                            s=str(chr(ord(BFS[i][0])+2))+str(int(BFS[i][1])-1)
                            temp.append(s)
                        if  ord(BFS[i][0])+2<=ord('h') and int(BFS[i][1])+1<=8:
                            s=str(chr(ord(BFS[i][0])+2))+str(int(BFS[i][1])+1)
                            temp.append(s)
                        if  ord(BFS[i][0])+1<=ord('h') and int(BFS[i][1])+2<=8:
                            s=str(chr(ord(BFS[i][0])+1))+str(int(BFS[i][1])+2)
                            temp.append(s)
                        if  ord(BFS[i][0])-1>=ord('a') and int(BFS[i][1])+2<=8:
                            s=str(chr(ord(BFS[i][0])-1))+str(int(BFS[i][1])+2)
                            temp.append(s)
                        if  ord(BFS[i][0])-2>=ord('a') and int(BFS[i][1])+1<=8:
                            s=str(chr(ord(BFS[i][0])-2))+str(int(BFS[i][1])+1)
                            temp.append(s)
                    #print(*temp)
                    if ed in temp:
                        print("To get from %s to %s takes %d knight moves."%(st,ed,count))
                        break
                    count+=1
                    BFS=temp
        except EOFError:
            break
main()