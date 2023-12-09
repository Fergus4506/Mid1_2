n=int(input())
dis=[2]
for i in range(3,201,2):
    ck=1
    for j in range(2,(int)(i**0.5)+1):
        if i%j==0:
            ck=0
            break
    if ck:
        dis.append(i)
for i in range(n):
    s=input()
    ans=[]
    for j in range(len(s)):
        if s[j] not in ans:
            t=s.count(s[j])
            if t in dis:
                ans.append(s[j])
    ans.sort()
    print("Case %d:"%(i+1),end=" ")
    if len(ans)==0:
        print("empty")
    else:
        print("".join(ans))
