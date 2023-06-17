encode=[]
key=[]

def find(key):
    pass
tree=[[6,1,0,2,3],[1,-1,"C",-1,0],[5,-1,"A",-1,0],[13,0,0,4,-1],[7,-1,"B",-1,3]]
rootpt=0

for i in range(len(tree)):
    # print(not str(tree[i][2]).isdigit(),tree[i][2])
    if not str(tree[i][2]).isdigit():
        key.append(i)
# print(*key)
        

for i in key:
    last=-1
    now=i
    temp=[]
    count=0
    while now!=-1:
        if last==-1:
            temp.append(tree[now][2])
            last=now
            now=tree[now][-1]
        else:
            if tree[now][1]==last:
                temp.insert(1,0)
            elif tree[now][3]==last:
                temp.insert(1,1)
            else:
                print("error")
            last=now
            now=tree[now][-1]
        print(now,last)
        count+=1

    print(temp)