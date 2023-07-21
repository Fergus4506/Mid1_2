#題目要求
#今天會給一連串的事件，這些事件以a-z來代表，算這些事件可以分開組合成的所有可能
#但是順序不能改變，不能略過前面的事件，且第一個和最後一個的事件在該組合中都要是唯一的
#注意:因為當頭尾的事件一重複就不能算了，所以複數個同字母重複事件可以視為但一事件
#ex:aabbc=>以第一個a為頭的話沒有任何一種組合，但第二個就可以正常判斷
#aabbc=>abc



n=list(input())
nCheck=[]
last=""

#這裡在做的就是把一樣的合併
for i in range(len(n)):
    if n[i]!=last:
        last=n[i]
        nCheck.append(n[i])

#這裡的寫法其實就是把每一個事件都當作開頭做一次，每有新的一種事件就標記起來
#當今天當作結尾的事件已經出現過了就忽略這個組合
#而且如果重複的事件是開頭事件的話就代表後面的組合都不合法了，所以以該事件為開頭
#的組合就只能算到這裡而已
ans=0
checkEngilsh=[0 for i in range(26)]#用來標記元素的陣列
# print(checkEngilsh)

for i in range(len(nCheck)):#一個一個拿來當作開頭元素

    checkEngilsh[ord(nCheck[i])-ord('a')]=1#先把開頭元素標記

    for j in range(i+1,len(nCheck)):#判斷結尾事件是否重複，如果都符合規則則ans+1
        now=ord(nCheck[j])-ord('a')

        if now==ord(nCheck[i])-ord('a'):#當現在判斷的事件是否與開頭重複，如果有直接退出
            break
        if checkEngilsh[now]!=1:#判斷是否與已出現過的事件重複
            checkEngilsh[now]=1
            ans+=1
    #print(checkEngilsh)
    checkEngilsh=[0 for i in range(26)]#重置標記

#下面這個寫法是裡面的所有的元素都不能重複的寫法，此問題的衍伸題目
# nCheck.reverse()
# for i in range(1,len(nCheck)):
#     now=nCheck[front:i]
#     print("".join(now))
#     print(nCheck[i])
#     if nCheck[i] in now:
#         print("@")
#         where=now.index(nCheck[i])
#         front=where+front+1
#     print(front)
#     nwans=nCheck[front:i]
#     print("".join(nwans))
#     ans+=len(nwans)
#     print()
#     # print("%d\n"%(ans))
print(ans)