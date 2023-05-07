def checkPaste(height):
    # 計算可以被貼的區段
    postLen = []
    long = 0
    for num in board:
        if num >= height:
            long += 1
        else:
            if long != 0:
                postLen.append(long)
                long = 0

    if long:
        postLen.append(long)

    # 依序看看已知的區段是否可以貼滿所有海報
    poindex = 0
    post = posts[poindex]
    for width in postLen:
        while width >= post:
            width -= post
            poindex += 1
            if poindex < len(posts):
                post = posts[poindex]
            else:
                return True

    return False
while True:
    try:
        n, k = map(int, input().split())
        board = list(map(int, input().split()))
        posts = list(map(int, input().split()))

        # 檢查貼上高度為 height 的貼紙是否能夠貼滿整個看板

        # 設定二分搜尋的範圍
        l = 1
        r = max(board)

        # 進行二分搜尋，尋找最大可行的高度
        while l <= r:
            mid = (l+r) // 2
            bePast = checkPaste(mid)
            if bePast:
                l = mid + 1
            else:
                r = mid - 1

        # 印出最大高度
        print(r)
    except EOFError:
        break