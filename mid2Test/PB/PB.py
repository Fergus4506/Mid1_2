while True:
    try:
        st=list(map(int,input().split()))
        goodP=list(map(int,input().split()))
        goodP.sort()
        gf=list(map(int,input().split()))
        gf.sort()
        i,j,ans=0,0,0
        while i<len(goodP) and j<len(gf):
            if goodP[i]>=gf[j]:
                ans+=goodP[i]
                j+=1
            else:
                i+=1
        print(ans)
            

    except EOFError:
        break