class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums.sort()
        ans = []
        for i in range(1,len(nums),2):
            ans.append(nums[i])
            ans.append(nums[i-1])
        return ans