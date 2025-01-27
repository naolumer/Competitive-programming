class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = []
        for i in range(1,len(nums)):
            d.append(abs(nums[i]-nums[i-1]))
        
        d.append(abs(nums[-1]-nums[0]))
        
        return max(d)