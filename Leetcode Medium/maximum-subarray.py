class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)
        cur_sum = 0
        max_sub_sum = -100000
        for i in range(n):
            cur_sum+=nums[i]
            max_sub_sum = max(cur_sum,max_sub_sum)

            if cur_sum < 0:
                cur_sum = 0
        return max_sub_sum