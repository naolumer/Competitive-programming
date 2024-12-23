def intersection(nums):
    dc = {}
    for arr in nums:
        for num in arr:
            if num in dc:
                dc[num]+=1
            else:
                dc[num] = 1
    answer = []
    for key,i in dc.items():
        if i == len(nums):
            answer.append(key)
    sortedd = sorted(answer)
    return sortedd