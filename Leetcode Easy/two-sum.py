def twoSum(nums, target):
        
        two_sum=[]

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    two_sum.append(i)
                    two_sum.append(j)
                    
        return two_sum

print(twoSum([2,3,4,5,6], 11))