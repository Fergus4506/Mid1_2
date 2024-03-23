while 1:
    n=int(input())
    if n==0:
        break
    print(f"Original number was {n}")
    chain=[]
    while True:
        if n in chain:
            break
        chain.append(n)
        small = sorted(str(n))
        big = small[::-1]
        first = int(''.join(big))
        second = int(''.join(small))
        print(f"{first} - {second} = {first - second}")
        n=first-second
    print(f"Chain length {len(chain)}\n")
#註解
#注意:循環的部分有可能是超過一個以上的數字
#所以要用一個list來存放每次的數字 
#而不是直接使用前一個數字來做比較    

# def get_next_number(n):
#     small = sorted(str(n))
#     big = small[::-1]
#     first = int(''.join(big))
#     second = int(''.join(small))
#     print(f"{first} - {second} = {first - second}")
#     return first - second

# def solve_uva_263(n):
#     chain = []
#     while True:
#         if n in chain:
#             break
#         chain.append(n)
#         n = get_next_number(n)
#     return chain

# while True:
#     n = int(input())
#     if n == 0:
#         break
#     print(f"Original number was {n}")
#     chain = solve_uva_263(n)
#     print(f"Chain length {len(chain)}\n")
    
