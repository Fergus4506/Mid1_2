# def checkFl(checkNumber):
#     c=checkNumber.split('.')
#     if len(c)>2:
#         return False
#     else:
#         for i in c:
#             if i.isdigit():
#                 pass
#             else:
#                 return False
#         return  True

n = input().split()
x=[]
while True:
    try:
        x.append(input().split())
    except:
        break

stack = []
ans = 0
for i in n:
    if i == ")":
        f, s = 0, 0

        check = False
        while len(stack) != 0:
            print(stack)
            print("%d %d"%(f,s))
            temp = stack.pop()
            if temp == "(":
                ans = s
                print(s)
                stack.append(str(s))
                break
            elif temp == "+":
                stack.append(str(f+s))
            elif temp == "-":
                stack.append(str(f-s))
            elif temp == "*":
                stack.append(str(f*s))
            elif temp == "/":
                stack.append(str(f//s))
            elif temp.isdigit():
                if check:
                    f = int(temp)
                    check = not check
                else:
                    s = int(temp)
                    check = not check
            else:
                tx=0
                for j in range(len(x)):
                    if temp==x[j][0]:
                        tx=int(x[j][2])
                if check:
                    f = tx
                    check = not check
                else:
                    s = tx
                    check = not check

    else:
        stack.append(i)
print(ans)

