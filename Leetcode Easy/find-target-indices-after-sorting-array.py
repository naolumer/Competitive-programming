def targetIndices(nums,target):
    sortedd = sorted(nums)
    answer = []
    for i in range(len(sortedd)):
        if sortedd[i] == target:
            answer.append(i)
    return answer