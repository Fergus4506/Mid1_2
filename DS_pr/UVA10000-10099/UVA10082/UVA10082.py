dis="`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"
while 1:
    try:
        n=input()
        temp=""
        for i in n:
            if i==" ":
                temp+=" "
            else:
                temp+=dis[dis.index(i)-1]
        print(temp)
    except EOFError:
        break