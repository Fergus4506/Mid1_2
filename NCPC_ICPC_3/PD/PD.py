n=int(input())
already=[n]
check=1
while n!=1:
    temp=0
    while n!=0:
        temp=temp+(n%10)**2
        n=n//10
    n=temp
    # print(already)
    # print(n)
    if n not in already:
        already.append(n)
    else:
        print("UNHAPPY")
        check=0
        break
if check:
    print("HAPPY")