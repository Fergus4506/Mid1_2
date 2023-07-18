n=int(input())
old=[]
for i in range(n):
    old.append(input())
new=[]
for i in range(n):
    new.append(input())

maxUp=0
ans=""
count=0
for i in range(n):
    compare=old.index(new[i])-new.index(new[i])
    # print(compare)
    if compare>maxUp:
        maxUp=compare
        ans=new[i]
        count=1
if not count:
    print("suspicious")
else:
    print(ans)