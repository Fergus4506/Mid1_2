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
def find_min(a, b, c):
    return min(a, b, c)

while True:
    try:
        num1, s1 = input().split()
        num2, s2 = input().split()
        num1 = int(num1)
        num2 = int(num2)
        graph = [[0 for _ in range(1000)] for _ in range(1000)]

        for i in range(1000):
            graph[0][i] = i
            graph[i][0] = i

        for i in range(1, num1 + 1):
            for j in range(1, num2 + 1):
                num_re = graph[i - 1][j - 1]
                if s1[i - 1] != s2[j - 1]:
                    num_re += 1
                graph[i][j] = find_min(num_re, graph[i - 1][j] + 1, graph[i][j - 1] + 1)

        print(graph[num1][num2])
    except EOFError:
        break