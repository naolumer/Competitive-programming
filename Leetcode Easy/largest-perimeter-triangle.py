class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largestP = 0
        nums.sort()
        for i in range(0,len(nums)-2):
            if (nums[i] + nums[i+1]) > nums[i+2] and (nums[i] + nums[i+2]) > nums[i+1] and (nums[i+1] + nums[i+2]) > nums[i] :
                largestP = max(largestP, nums[i] + nums[i+1] + nums[i+2])
        return largestP