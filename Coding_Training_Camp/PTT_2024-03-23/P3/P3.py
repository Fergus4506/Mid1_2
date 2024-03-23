n=int(input())
name_list=[]
for i in range(n):
    temp=input().split()
    check=1
    for j in range(len(name_list)):
        if temp[0]==name_list[j][0]:
            name_list[j][1]+=1
            check=0
            break
    if check:
        name_list.append([temp[0],1])
name_list.sort(key=lambda x:x[0])
for i in range(len(name_list)):
    print(f"{name_list[i][0]} {name_list[i][1]}")
