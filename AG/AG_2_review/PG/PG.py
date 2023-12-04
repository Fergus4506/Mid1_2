while 1:
    try:
        s1=input()
        s2=input()
        grid=[[0 for j in range(min(len(s1),len(s2))+1)] for i in range(max(len(s1),len(s2))+1)]
        for i in range(1, max(len(s1),len(s2)) + 1):
            for j in range(1, min(len(s1),len(s2)) + 1):
                if len(s1)>len(s2):
                    if s1[i - 1] == s2[j - 1]:
                        grid[i][j] = grid[i - 1][j - 1] + 1#i跟j都減1是因為需要知道前面有幾個相同的(調dp表來看)
                    else:
                        grid[i][j] = 0
                else:
                    if s2[i - 1] == s1[j - 1]:
                        grid[i][j] = grid[i - 1][j - 1] + 1
                    else:
                        grid[i][j] = 0
        print(grid)
    except EOFError:
        break