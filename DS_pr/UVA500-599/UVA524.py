count=1
def dfs(pre,n):
    #print(*pre)
    if len(pre)==n:
        print(*pre)
        return None
    for i in range(2,n+1):
        temp=pre[:]
        if i not in pre and (pre[len(pre)-1]%i!=0 or i%pre[len(pre)-1]!=0):
            temp.append(i)
            dfs(temp,n)
while True:
    try:
        n=int(input())
        dfs([1],n)
    except EOFError:
        break