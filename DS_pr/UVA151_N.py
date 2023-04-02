while True:
    try:
        n=int(input())
        if n==0:
            break
        grid=[]
        for i in range(n):
            grid.append([i+1,0])
        
    except EOFError:
        break