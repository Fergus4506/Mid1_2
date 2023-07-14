n=int(input())
grid=[]
temp=input().split()
for i in range(n):
    if temp[i]=="T":
        grid.append(1)
    else:
        grid.append(0)
step=input().split()
stack=[]
for i in range(len(step)):
    if step[i]=="-":
        t=stack.pop()
        t=(t+1)%2
        stack.append(t)
    elif step[i]=="+":
        t1,t2=stack.pop(),stack.pop()
        # print(t1,t2)
        if t1==1 or t2==1:
            stack.append(1)
        else:
            stack.append(0)
    elif step[i]=="*":
        t1,t2=stack.pop(),stack.pop()
        if t1==1 and t2==1:
            stack.append(1)
        else:
            stack.append(0)
    else:
        stack.append(grid[ord(step[i])-ord('A')])
ans=stack.pop()
if ans:
    print("T")
else:
    print("F")