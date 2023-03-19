
#preorder最前面一定是目前樹狀圖的根結點
#找到根節點後可以用inorder該值去判斷哪些元素是他左側的，哪些是他右側的
#最後再利用遞迴去把大樹拆成小樹，而這個過程跟後續走訪其實很像
#所以當觸底後就可以輸出葉子的值讓整棵樹以後序的方式來表現
def printPre(preorder,inorder):
    if not preorder:
        return None

    index=inorder.index(preorder[0])

    printPre(preorder[1:index+1],inorder[:index])
    printPre(preorder[index+1:],inorder[index+1:])

    print(preorder[0],end="")

n=int(input())
for i in range(n):
    List=input().split()
    length=int(List[0])
    pre_order=list(List[1])
    in_order=list(List[2])
    printPre(pre_order,in_order)
    print()
    