while 1:
    try:
        s1=input()
        s2=input()
        ans=0
        grid=[[0 for j in range(min(len(s1),len(s2))+1)] for i in range(max(len(s1),len(s2))+1)]
        for i in range(1, max(len(s1),len(s2)) + 1):
            for j in range(1, min(len(s1),len(s2)) + 1):
                if len(s1)>len(s2):
                    if s1[i - 1] == s2[j - 1]:
                        grid[i][j] = grid[i - 1][j - 1] + 1#i跟j都減1是因為需要知道前面有幾個相同的(調dp表來看)
                    else:
                        grid[i][j] = max(grid[i-1][j],grid[i][j-1])
                else:
                    if s2[i - 1] == s1[j - 1]:
                        grid[i][j] = grid[i - 1][j - 1] + 1
                    else:
                        grid[i][j] = max(grid[i-1][j],grid[i][j-1])
                if grid[i][j]>ans:
                    ans=grid[i][j]
        print(ans)
    except EOFError:
        break