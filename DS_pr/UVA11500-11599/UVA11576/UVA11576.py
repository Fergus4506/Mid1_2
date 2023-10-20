try:
    while 1:
        n=int(input())
        for i in range(n):
            m,n=map(int,input().split())
            sum=m
            all=[]
            for j in range(n):
                all.append(input())
                if j==0:
                    continue
                temp=0
                now_str=all[j]
                last_str=all[j-1]
                # print(now_str,last_str)
                for k in range(m):
                    if now_str[:k+1]==last_str[m-k-1:]:
                        temp=k+1
                sum+=m-temp
            print(sum)
except EOFError:
    pass
