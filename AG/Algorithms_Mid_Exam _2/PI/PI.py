while 1:
    try:
        N=int(input())
        check=N%7
        if(check==0):
            print("Hello World!")
        else:
            if(check%2):
                print("Hello World!")
                print("Hello World!")
            else:
                print("Hello World!")
                print("Hello World!")
                print("Hello World!")
    except EOFError:
        break