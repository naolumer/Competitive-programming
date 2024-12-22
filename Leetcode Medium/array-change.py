def arrayChange(nums, operations):
        dc = {val:i for i,val in enumerate(nums)}
        for op in operations:
            n1,n2 = op
            nums[dc[n1]] = n2
            dc[n2] = dc[n1]
        return nums