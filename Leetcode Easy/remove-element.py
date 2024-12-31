class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        m = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[m] = nums[i]
                m+=1

                
        return m