#(A*B)%M=A%M+B%M
#而幾次方=N*N**(M-1),N為底數，M為次方數
#所以可以用遞迴的方式來將次方一個一個慢慢拆到1或0後再做運算
#這樣就可以算出來

def BigMod(B,P,M):
    if P==0:
        return 1
    elif P==1:
        return B%M
    else:
        rs=BigMod(B,P//2,M)
        if P%2:
            return (rs*rs*B)%M#因為不整除，會多出一個B沒算到要還給他
        else:
            return (rs*rs)%M
count=0
while True:
    try:
        if count:
            b=input()
        B=int(input())
        P=int(input())
        M=int(input())
        if M==1:#如果%1的話所有數字的餘數皆為0
            print(0)
        else:
            print(BigMod(B,P,M))
        count=1
    except EOFError:
        break
