import random
e=int(input())
p,q=map(int,input().split())
M=input()
n=p*q
# e=
MChangeGrid=""
for i in M:
    if i==" ":
        MChangeGrid+="26"
    else:
        MChangeGrid+=str(ord(i)-ord('A')).zfill(2)
print(MChangeGrid)