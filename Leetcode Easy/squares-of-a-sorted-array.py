class Solution:

    # O(n) solution using two pointers
    def sortedSquares(self, nums: List[int]) -> List[int]:
        index = len(nums)-1
        left = 0
        right = len(nums)-1
        result = [0]*len(nums)

        while left<=right:
            if abs(nums[left]) > abs(nums[right]):
                result[index]=nums[left]**2
                left+=1
            else:
                result[index]=nums[right]**2
                right-=1
            index-=1
        return result