def chToBr(n):
    s=""
    while n!=0:
        s=str(n%2)+s
        n=n//2
    return s
def cuToTwo(s):
    l=len(s)//2
    A1=s[:l]
    A2=s[l:]
    h1=0
    # print(A1)
    # print(A2)
    for i in range(2,l-2):
        if A1[i]!=A2[i]:
            h1=h1*2+1
        else:
            h1=h1*2
    return h1
def cuTotre(s):
    l=len(s)//3
    B1=s[:l]
    B2=s[l:l*2]
    B3=s[l*2:]
    temp,h2,check="",0,0
    for i in range(l):
        if B1[i]!=B3[i]:
            temp=temp+"1"
        else:
            temp=temp+"0"
    # print(temp)
    for i in range(l):
        if B2[i]!=temp[i]:
            h2=h2*2+1
        else:
            h2=h2*2
    return h2
while True:
    try:
        n=int(input())
        Sn=chToBr(n)
        # print(Sn)
        Cun=cuToTwo(Sn)
        # print(Cun)
        Tun=cuTotre(Sn)
        # print(Tun)
        print(Cun,Tun)
    except EOFError:
        break