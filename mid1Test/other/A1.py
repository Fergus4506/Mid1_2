import copy
def change(s,x):
    if x+1==len(s):
        print(s)
        return 0
    else:
        change(s,x+1)
        for i in range(x+1,len(s)):
            temp=copy.deepcopy(s)
            t=temp[x]
            temp[x]=temp[i]
            temp[i]=t
            change(temp,x+1)
            
s=list(input())
change(s,0)

