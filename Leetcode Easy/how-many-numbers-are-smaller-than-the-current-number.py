def smallerNumbersThanCurrent(nums):

    # not as fast due to (nums2.index(items)) O(n^2)
    # nums2 = sorted(nums)
    # dc = {item: nums2.index(item) for item in nums2}
    # return [dc[num] for num in nums]

    # faster (O(nlogn))

    
    nums2 = sorted(nums)
    
    dc = {}
    for i, val in enumerate(nums2):
        
        dc[val] = i
    return [dc[num] for num in nums]

    