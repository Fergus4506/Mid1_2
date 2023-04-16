#給過但會超時，因為此方法為以C++為底來設想的方法
n=int(input())
grid=[2]
for i in range(3,40000,2):
    check=1
    for j in range(3,int(i**0.5)+1):
        if i%j==0:
            check=0
            break
    if check:
        grid.append(i)
for i in range(n):
    ans=[1,1]
    s,e=map(int,input().split())
    for j in range(s,e+1):
        temp=j
        tpAn=1
        if j in grid:
            tpAn=2
        elif j==1:
            tpAn=1
        else:
            temp=j
            for x in range(2,int(j**0.5)+1):
                count=0
                if x in grid and temp%x==0:
                    count=0
                    while temp%x==0:
                        temp=temp//x
                        count+=1
                    tpAn*=count+1
                if temp==1:
                    break
            if temp>1:
                tpAn*=2
            if tpAn>ans[1]:
                ans=[j,tpAn]
        if tpAn>ans[1]:
            ans=[j,tpAn]
    print("Between %d and %d, %d has a maximum of %d divisors."%(s,e,ans[0],ans[1]))

#這個是python遞迴的版本，基本概念相同但是沒有建表反而是以遞迴查找的方式來實現
# from math import sqrt
# from collections import Counter
# def primeFactors(n):
#     i = 2
#     while i<= sqrt(n):
#         if n%i == 0:
#             l = primeFactors(n/i)
#             l.append(i)
#             return l 
#         i+=1
#     return [n]

# numTest = int(input())

# for itertest in range(numTest):
#     L,U = map(int,input().split())
#     it = L 
#     result,maxI = 0,-1
    
#     while it<=U:
#         f = primeFactors(it)
#         counter = Counter(f)
#         result1 = 1
        
#         for c in counter:
#             result1 *= counter[c] + 1
#         if result1 > result:
#             result = result1
#             maxI = it 
#         it+=1
#     if L == 1 and U == 1:  
#         print("Between %d and %d, %d has a maximum of 1 divisors."%(L,U,maxI))
#     else:
#         print("Between %d and %d, %d has a maximum of %d divisors."%(L,U,maxI,result))

