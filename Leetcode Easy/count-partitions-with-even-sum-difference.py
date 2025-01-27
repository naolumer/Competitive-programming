class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        n = len(nums)

        for i in range(len(nums)-1):
            s = sum(nums[0:i+1]) - sum(nums[i+1:n])
            if s%2==0:
                counter+=1
        return counter