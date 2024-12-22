def maximumCount(nums):
    pos_count =0
    neg_count = 0

    low,high = 0,len(nums)-1

    while low<=high:
        mid = (low+high)//2

        if nums[mid] > 0:
            pos_count = len(nums)-mid
            high = mid -1
        else:
            low = mid + 1
    
    high,low = len(nums)-1,0
    while low<=high:
        mid = (low+high)//2

        if nums[mid] < 0:
            neg_count = mid + 1
            low = mid+1
        else:
            high = mid - 1
    return max(neg_count,pos_count) 