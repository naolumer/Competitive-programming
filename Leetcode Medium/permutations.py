class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        sol = []

        def backtrack():
            if len(sol)==len(nums):
                res.append(sol[:])
                return
            
            for i in nums:
                if not i in sol:
                    sol.append(i)
                    backtrack()
                    sol.pop()
        backtrack()
        return res