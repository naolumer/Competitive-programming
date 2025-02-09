class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res= []
        sol = []
        nums = candidates
        n = len(nums)

        def backtrack(i,cur_sum):
            if target == cur_sum:
                res.append(sol[:])
                return
            
            if i==n or  target < cur_sum:
                return
            
            backtrack(i+1,cur_sum)
            sol.append(nums[i])
            backtrack(i,cur_sum + nums[i])
            sol.pop()
        backtrack(0,0)
        return res