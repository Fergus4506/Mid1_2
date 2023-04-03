# dt={0:"",1:"stack",2:"queue",3:"priority queue",4:"not sure"}
# ans=[]
# while True:
#     try:
#         n=int(input())
#         step=[]
#         grid=[]
#         for i in range(n):
#             step.append(list(map(int,input().split())))
#         maxN=-2**100
#         last=0
#         lastS=-1
#         check=1
#         error=1
#         for i in range(n):
#             if step[i][0]==1:  
#                 grid.append(step[i][1])
#                 if maxN<step[i][1]:
#                     maxN=step[i][1]
#             elif step[i][0]==2:
#                 if len(grid)==0 or step[i][1] not in grid:
#                     error=0
#                     ans.append("impossible")
#                     break
#                 else:
#                     now=grid.index(step[i][1])
#                     tl=0
#                     tls=0
#                     if step[i][1]==maxN and lastS!=0:
#                         if len(grid)!=1:
#                             if now==len(grid)-1 and last!=3: 
#                                 tl=4
#                                 tls=2
#                             elif now==0 and last!=3:
#                                 tl=4
#                                 tls=1
#                             else:
#                                 tl=3
#                                 tls=-1
#                         else:
#                             tl=last
#                             tls=lastS
#                     else:
#                         if len(grid)!=1:
#                             if now==0:
#                                 tl=2
#                             elif now==len(grid)-1:
#                                 tl=1
#                         else:
#                             tl=last
#                             tls=lastS
#                     #print("%d %d t"%(tl,tls))
#                     if check:
#                         last=tl
#                         lastS=tls
#                         check=0
#                     else:
#                         if last!=tl:
#                             if last!=tls:
#                                 ans.append("impossible")
#                                 error=0
#                                 break
#                             else:
#                                 last=tls
#                                 lastS=0
#                         elif lastS!=tls:
#                             ans.append("impossible")
#                             error=0
#                             break
#                     grid.pop(now)
#                     maxN=-2**100
#             for j in range(len(grid)):
#                 maxN=max(maxN,grid[j])

#             #print("%d %d"%(last,lastS))
#         if error:
#             if last==0 and lastS==-1:
#                 ans.append(dt[4])
#             else:
#                 ans.append(dt[last])
#     except EOFError:
#         break
# for i in range(len(ans)):
#     print(ans[i])
while True:
    try:
        stack=[]
        queue=[]
        pqueue=[]
        checkS,checkQ,checkP=1,1,1
        n=int(input())
        error=0
        for i in range(n):
            step=list(map(int,input().split()))
            if step[0]==1:
                stack.append(step[1])
                queue.append(step[1])
                pqueue.append(step[1])
                pqueue.sort()
            else:
                if len(stack)==0:
                    error=1
                else:
                    if stack.pop()!=step[1]:
                        checkS=0
                    if queue.pop(0)!=step[1]:
                        checkQ=0
                    if pqueue.pop()!=step[1]:
                        checkP=0
        if error:
            print("impossible")
            continue
        if (checkS and checkQ) or (checkS and checkP) or (checkQ and checkP):
            print("not sure")
        elif checkS:
            print("stack")
        elif checkP:
            print("priority queue")
        elif checkQ:
            print("queue")
        else:
            print("impossible")
    except EOFError:
        break