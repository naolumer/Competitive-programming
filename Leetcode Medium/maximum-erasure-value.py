def maximumUniqueSubarray(self, nums):

    seen = set()
    left = 0
    max_sum = 0
    cur_sum = 0

    for right in range(len(nums)):
        while nums[right] in seen:
            cur_sum -= nums[left]
            seen.remove(nums[left])
            left += 1
        cur_sum += nums[right]
        seen.add(nums[right])
        max_sum = max(max_sum, cur_sum)
    return max_sum
