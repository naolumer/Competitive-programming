def findPeakElement(nums):

    low,high = 0, len(nums)-1

    while low<=high:
        mid = (low+high)//2

        mid_val = nums[mid]
        to_left = nums[mid-1] if mid >0 else float("-inf")
        to_right = nums[mid + 1] if mid < len(nums)-1 else float("-inf")

        if to_left < mid_val > to_right:
            return mid
        elif to_left < mid_val<to_right:
            low = mid + 1
        else:
            high = mid-1
# O(logn) Binary Search
            