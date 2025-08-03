class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        
        prev, cur = nums[0], max(nums[0],nums[1])

        for i in range(2,n):
            prev, cur = cur, max(cur, nums[i] + prev)
        
        return cur