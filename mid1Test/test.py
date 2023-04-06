check = 1
no = 1
while True:
    try:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break

        if check:
            check = 0
        else:
            print()
        field = []
        for i in range(n):  # n*m的二維陣列
            subchar = []
            char = input()
            for j in range(len(char)):
                subchar.append(char[j])
            field.append(subchar)

        #print(field)確認資料是否正常存入

        ansfield = []
        for i in range(n):
            temp = []
            for j in range(m):
                if field[i][j] != "*":
                    count = 0
                    #print("%d %d"%(i,j))確認哪一個點出問題
                    if j == 0 and i == 0:  # 左上
                        if field[i][j+1] == "*":
                            count += 1
                        if field[i+1][j] == "*":
                            count += 1
                        if field[i+1][j+1] == "*":
                            count += 1
                    elif j == 0 and i == n-1:  # 左下
                        if field[i-1][j] == "*":
                            count += 1
                        if field[i-1][j+1] == "*":
                            count += 1
                        if field[i][j+1] == "*":
                            count += 1
                    elif j == m-1 and i == 0:  # 右上
                        if field[i][j-1] == "*":
                            count += 1
                        if field[i+1][j] == "*":
                            count += 1
                        if field[i+1][j-1] == "*":
                            count += 1
                    elif j == m-1 and i == n-1:  # 右下
                        if field[i-1][j] == "*":
                            count += 1
                        if field[i-1][j-1] == "*":
                            count += 1
                        if field[i][j-1] == "*":
                            count += 1
                    elif j == 0 and i != 0 and i != n-1:  # 第一行
                        if field[i-1][j] == "*":
                            count += 1
                        if field[i-1][j+1] == "*":
                            count += 1
                        if field[i][j+1] == "*":
                            count += 1
                        if field[i+1][j] == "*":
                            count += 1
                        if field[i+1][j+1] == "*":
                            count += 1
                    elif j == m-1 and i != 0 and i != n-1:  # 最後一行
                        if field[i-1][j-1] == "*":
                            count += 1
                        if field[i-1][j] == "*":
                            count += 1
                        if field[i][j-1] == "*":
                            count += 1
                        if field[i+1][j-1] == "*":
                            count += 1
                        if field[i+1][j] == "*":
                            count += 1
                    elif i == 0 and j != 0 and j != m-1:  # 第一列
                        if field[i][j-1] == "*":
                            count += 1
                        if field[i][j+1] == "*":
                            count += 1
                        if field[i+1][j-1] == "*":
                            count += 1
                        if field[i+1][j] == "*":
                            count += 1
                        if field[i+1][j+1] == "*":
                            count += 1
                    elif i == n-1 and j != 0 and j != m-1:  # 最後一列
                        if field[i-1][j-1] == "*":
                            count += 1
                        if field[i-1][j] == "*":
                            count += 1
                        if field[i-1][j+1] == "*":
                            count += 1
                        if field[i][j-1] == "*":
                            count += 1
                        if field[i][j+1] == "*":
                            count += 1
                    else:  # 其他地方
                        if field[i-1][j-1] == "*":
                            count += 1
                        if field[i-1][j] == "*":
                            count += 1
                        if field[i-1][j+1] == "*":
                            count += 1
                        if field[i][j-1] == "*":
                            count += 1
                        if field[i][j+1] == "*":
                            count += 1
                        if field[i+1][j-1] == "*":
                            count += 1
                        if field[i+1][j] == "*":
                            count += 1
                        if field[i+1][j+1] == "*":
                            count += 1
                    temp.append(count)
                else:
                    temp.append("*")
            ansfield.append(temp)

        print("Field #%d:" % (no))
        for i in range(n):
            for j in range(m-1):
                print(ansfield[i][j], end="")
            print(ansfield[i][m-1])
        no += 1
    except EOFError:
        break
