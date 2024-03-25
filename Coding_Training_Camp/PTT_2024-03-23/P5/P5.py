# while 1:
#     try:
#         A=input().split()
#         A=A[1]
#         B=input().split()
#         B=B[1]
#         dp=[[0 for i in range(len(B)+1)] for j in range(len(A)+1)]
#         # print(dp)
#         for i in range(len(A)-1,-1,-1):
#             for j in range(len(B)-1,-1,-1):
#                 if A[i]==B[j]:
#                     dp[i][j]=max(dp[i+1][j],dp[i][j+1],dp[i+1][j+1]+1)
#                 else:
#                     dp[i][j]=max(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])
#         # print(dp)
#         print(max(len(A),len(B))-dp[0][0])
#     except EOFError:
#         break
# def LCS(A, B):
#     dp = [[0 for i in range(len(B) + 1)] for j in range(len(A) + 1)]
#     for i in range(len(A) - 1, -1, -1):
#         for j in range(len(B) - 1, -1, -1):
#             if A[i] == B[j]:
#                 dp[i][j] = max(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1] + 1)
#             else:
#                 dp[i][j] = max(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
#     return dp[0][0]

# while True:
#     try:
#         A = input().split()
#         A = A[1]
#         B = input().split()
#         B = B[1]
#         print(max(len(A), len(B)) - LCS(A, B))
#     except EOFError:
#         break
def LCS(A, B):
    dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
    for i in range(len(A) - 1, -1, -1):
        for j in range(len(B) - 1, -1, -1):
            if A[i] == B[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[0][0]

while True:
    try:
        A = input().strip()
        B = input().strip()
        print(max(len(A) , len(B)) - LCS(A, B))
    except EOFError:
        break