dir=[]
while True:
    n=input().split()
    if n[0]=="#":
        break
    for i in n:
        dir.append(i)
ans=[]
# print(dir)
for i in range(len(dir)):
    t=list(dir[i].lower())
    t.sort()
    check=True
    for j in range(len(dir)):
        if j==i:
            continue
        tc=list(dir[j].lower())
        tc.sort()
        if len(t)!=len(tc):
            continue
        else:
            checkN=True
            for x in range(len(t)):
                if t[x]!=tc[x]:
                    checkN=False
                    break
        if checkN:
            check=False
    if check:
        ans.append(dir[i])
ans.sort()
for i in range(len(ans)):
    print(ans[i])