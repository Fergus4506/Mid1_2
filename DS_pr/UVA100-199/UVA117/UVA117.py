while True:
    try:
        grid=[]
        ans=0
        while True:
            t=input()
            if t=="deadend":
                break
            grid.append(t)
            ans+=len(t)
        print(ans)
    except EOFError:
        break