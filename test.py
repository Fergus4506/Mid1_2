start = list(map(int, input().split())) 
end = list(map(int, input().split())) 
len_start = len(start) 
rv_start = start[::-1] 
rv_start.sort(reverse=True) 
ans=[]
ck=0 
rd=0
while 1: 
    if start == end:
        ck=1 
        ans.append(start)
        break 
    if start == rv_start: 
        break 
    ans.append(start)
    last = start[len_start - 1] 
    changePs = 0 
    for i in range(len_start - 2, -1, -1): 
        if start[i] < last: 
            changePs = i 
            break 
        last = start[i] 
    temp = start[changePs + 1:] 
    start = start[:changePs + 1] 
    temp.sort() 
    for i in range(len(temp)): 
        if temp[i] > start[changePs]: 
            start[changePs], temp[i] = temp[i], start[changePs] 
            break 
    start = start + temp 
    rd +=1
if ck:
    for i in ans: 
        print(i) 