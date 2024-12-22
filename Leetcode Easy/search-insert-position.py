def searchInsert(nums, target):
        
    low,high = 0, len(nums)-1

    while high>=low:
        mid = (low + high)//2  

        if nums[mid] == target:
            return mid
        elif nums[mid]>target:
            high = mid-1
        else:
            low = mid + 1
    return low