def runningSum(nums):
    fnum = nums[0]
    answer = [fnum]
    for i in range(1,len(nums)):
        ff = fnum + nums[i]
        answer.append(ff)
        fnum = ff
        
    return answer