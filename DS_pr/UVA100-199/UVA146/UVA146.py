#題目需求:給定一個由小寫字母組成的字串=>求該字串的下一個排序，
#如果該排序為最後一個或者是不可能實現的字串，輸出No Successor
#ex:abc->acb->bac->bca->cab->cba->No Successor

#這種排序原本是要利用DFS的方式來找出所有的排列組合再去找下一個
#但是這種題目其實找的到規律
#假設今天是 a d c b =>可以發現後面三個的 d c b 已經是最大的組合了
#所以要動一定會是 a ，但怎麼去動它呢
#由上面acb的排序我們可以知道當後面為最大組合後，去找 a 的下一個最小值
#也就是先用 b 與 a 交換，交換後再把後面的元素去排序就可以了

#這題要注意:
#有重複的問題，就像是 aacbb->ababc，這樣要注意一碰到符合條件就要跳出


def next_permutation(grid):

    changeplace=len(grid)-1#去分點(去分哪些需要改變哪些不用)

    for i in range(len(grid)-2,-1,-1):
        #確定目前的值是否還是在遞增的序列中，也就是cba這種最大序列排序的模式
        #當今天一出現不符合的地方後，就可已確定前面的東西不用改變，
        #只須改變後面的就好了
        if ord(grid[i])<ord(grid[i+1]):
            changeplace=i
            break
    
    minplace=changeplace+1#找出要與區分點交換的值

    for i in range(changeplace+2,len(grid)):
        #交換點要符合比區分點大且是在那個序列中最小的值
        if ord(grid[minplace])>ord(grid[i]) and ord(grid[i])>ord(grid[changeplace]):
            minplace=i
    if minplace==len(grid):#今天如果沒有找到交換點，就代表此序列為最大排序或不存在
        return "No Successor"
    # print(changeplace,minplace)

    #先交換兩點的值
    grid[changeplace],grid[minplace]=grid[minplace],grid[changeplace]
    # print(grid)

    #交換完後再去排序後面的元素
    temp=grid[changeplace+1:]
    temp.sort()
    # print(temp)
    ans=[]

    #在把兩者相加後合成為陣列輸出就可以了
    for i in range(changeplace+1):
        ans.append(grid[i])
    for i in range(len(temp)):
        ans.append(temp[i])
    return ''.join(ans)

            


while 1:
    n=input()
    ansGrid=[]
    if n[0]=="#":
        break
    print(next_permutation(list(n)))
    
    
