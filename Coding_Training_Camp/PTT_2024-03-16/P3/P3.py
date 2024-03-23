n=int(input())
for i in range(n):
    x=int(input())
    car_list=[]
    for j in range(x):
        temp=input().split()
        temp[1]=int(temp[1])
        temp[2]=int(temp[2])
        car_list.append(temp)
    
    y=int(input())
    cs_list=[]
    for j in range(y):
        cs_list.append(int(input()))
    for j in range(len(cs_list)):
        check=0
        ans=""
        for k in range(len(car_list)):
            if cs_list[j]>=car_list[k][1] and cs_list[j]<=car_list[k][2]:
                check+=1
                ans=car_list[k][0]
                if check>1:
                    break
                
        if check!=1:
            print("UNDETERMINED")
        else:
            print(ans)