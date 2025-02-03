class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_num1 = 0
        for i in range(len(nums)):
            if nums[i]>max_num1:
                max_num1 = nums[i]
        
        nums.pop(nums.index(max_num1))
        max_num2 = 0
        for i in range(len(nums)):
            if nums[i]>max_num2:
                max_num2 = nums[i]
        return (max_num1-1) * (max_num2-1)