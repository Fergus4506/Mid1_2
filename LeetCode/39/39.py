# Combination Sum
# Companies
# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

#題目大意:給你一個不規則的陣列，再給你一個目標數字，求陣列裡的元素有幾中相加方式可以達到目標數字，數字可重複使用
#陣列中最多150個元素且元素不重複
#注意:有沒有答案的可能，這種情況要回傳空陣列

class Solution:
    def my_count(now,nowgrid,grid,index,ans,target):
        print(nowgrid)
        for i in range(index,len(grid)):#這裡要注意的是從index開始跑而不是index+1是因為可以無限制地重複
            if now+grid[i]==target:#如果符合就把答案推進最後回傳的陣列中
                tgrid=nowgrid[:]
                tgrid.append(grid[i])
                ans.append(tgrid)
            elif now+grid[i]<target:#如果還小於目標數字代表可以繼續相加所以去跑下一層的地回
                tgrid=nowgrid[:]
                tgrid.append(grid[i])
                Solution.my_count(now+grid[i],tgrid,grid,i,ans,target)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        t=[]
        Solution.my_count(0,[],candidates,0,t,target)
        return t