n=int(input())
for i in range(n):
    k=int(input())
    name=input().split()
    temp=[]
    while len(name)!=1:
        temp.append(name.pop(0))
        temp.append(name.pop(0))
        name.append(temp.pop(0))
        name.append(temp.pop(0))
        name.pop(0)
    print(name[0])
        