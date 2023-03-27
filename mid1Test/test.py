def checkOrder(proder,midorder):
    if len(proder)==1:
        print(proder[0])
    now=midorder.index(proder[0])
    checkOrder(proder[1:],)
n=int(input())
for i in range(n):
    temp=input().split()
    proder=temp[1]
    midorder=temp[2]
