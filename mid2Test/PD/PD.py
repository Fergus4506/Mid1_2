import math
while True:
    try:
        n=int(input())
        node=[]
        for i in range(n):
            node.append(list(map(int,input().split())))
        
    except EOFError:
        break