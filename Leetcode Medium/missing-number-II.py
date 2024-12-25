def singleNumber(nums):
    count  = Counter(nums)

    for key,val in count.items():
        if val==1:
            return key