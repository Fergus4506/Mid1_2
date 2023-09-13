# 14.Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints(約束條件):
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

from ast import List#ast是一個強化樹狀結構程式撰寫的函式庫

#我的作法
#利用前綴只要有一個不一樣後面就都不算的這個特性
#最多相似的字串不會比題目給的字串中最短的字串還要常
#=>所以先去找最短的字串是誰
#=>再去跑那個字串長度的迴圈去判斷相同位置的字母是否相同，一旦一不相同就跳出並且丟出答案
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        minlen=201#設201是因為題目給的最長字串只會到200，所以要判斷誰會比他小的話設201就是最好的

        #找最短的字串
        for i in range(len(strs)):
            if len(strs[i])<minlen:
                minlen=len(strs[i])

        #判斷最大相同前綴
        for i in range(minlen):
            now=strs[0][i]
            count=1
            print(now)
            for j in range(1,len(strs)):
                if strs[j][i]!=now:
                    break
                count+=1
            if count==len(strs):
                ans+=now
            else:
                break
        return ans
    
#以下為天才作法
#因為可以知道如果所有字串用ASCII來排序的話排序前端如果不相同可能就會排到最前面或最後面
#而有部分相同的字串一定會排在一起
#ex:[“preheat”,”oven”,”prehistoric”]
#排序後=>["oven", "preheat", "prehistoric"].(因為有某部分相同所以最後兩個會比較靠近而沒有相似的就會跳出來)
#所以最後只要比較第一個和最後一個就好了(假設都有部分相同最多不一樣的會跑到最後)
# class Solution:
#     def longestCommonPrefix(self, v: List[str]) -> str:
#         ans=""
#         v=sorted(v)
#         first=v[0]
#         last=v[-1]
#         for i in range(min(len(first),len(last))):
#             if(first[i]!=last[i]):
#                 return ans
#             ans+=first[i]
#         return ans 