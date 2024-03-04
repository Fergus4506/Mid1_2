# while 1:
#     try:
#         s1=input()
#         s2=input()
#         grid=[[0 for i in range(len(s1)+1)] for j in range(len(s2)+1)]
#         grids=[["" for i in range(len(s1)+1)] for j in range(len(s2)+1)]
#         ans=[]
#         maxlen=0
#         for i in range(len(s2)+1):
#             for j in range(len(s1)+1):
#                 t1,t2=0,0
#                 ts1,ts2='',''
#                 if i-1>-1:
#                     t1=grid[i-1][j]
#                     ts1=grids[i-1][j]
#                 if j-1>-1:
#                     t2=grid[i][j-1]
#                     ts2=grids[i][j-1]
#                     print(grids[i][j-1])
#                 print(t1,ts1,t2,ts2)
#                 if j-1>-1 and i-1>-1:
#                     grid[i][j]=max(t1,t2)+(1 if s1[j-1]==s2[i-1] else 0)
#                     grids[i][j]=ts2 if t2>t1 else ts1
#                     grids[i][j]=grids[i][j]+s1[j-1] if s1[j-1]==s2[i-1] else ""
#                 else:
#                     grid[i][j]=max(t1,t2)
#                     grids[i][j]=ts2 if t2>t1 else ts1
#                 if grid[i][j]>maxlen:
#                     ans=[]
#                     ans.append(grids[i][j])
#                     maxlen=grid[i][j]
#                 elif grid[i][j]==maxlen and grids[i][j] not in ans:
#                     ans.append(grids[i][j])
#         print(grids)
#     except EOFError:
#         break
