while True:
    try:
        std = list(map(int, input().split()))
        grid = list(map(int, input().split()))

        inser = grid[:]
        print(1)
        for i in range(std[1]):
            if i < len(grid):
                for j in range(i, 0, -1):
                    if inser[j] > inser[j-1]:
                        inser[j], inser[j-1] = inser[j-1], inser[j]
                    else:
                        break
            for j in range(len(grid)):
                if j == len(inser)-1:
                    print(inser[j], end="")
                else:
                    print(inser[j], end=" ")
            print()

        print(2)
        bb = grid[:]
        for i in range(std[1]):
            if i < len(grid):
                for j in range(len(bb)-1, i, -1):
                    if bb[j] > bb[j-1]:
                        bb[j], bb[j-1] = bb[j-1], bb[j]
            for j in range(len(grid)):
                if j == len(bb)-1:
                    print(bb[j], end="")
                else:
                    print(bb[j], end=" ")
            print()
            
        print(3)
        sl = grid[:]
        for i in range(std[1]):
            if i < len(grid):
                maxIndex = i
                for j in range(len(bb)-1, i, -1):
                    if sl[j] > sl[maxIndex]:
                        maxIndex = j
                sl[maxIndex], sl[i] = sl[i], sl[maxIndex]
            for j in range(len(grid)):
                if j == len(inser)-1:
                    print(sl[j], end="")
                else:
                    print(sl[j], end=" ")
            print()
    except EOFError:
        break
