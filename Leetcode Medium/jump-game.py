
def CanJump(nums):

    goal = len(nums)-1

    for i in range(len(nums)-1,-1,-1):
        if i + nums[i] >= goal:
            goal = i
    return goal ==0
    
# print(CanJump([3,2,1,0,4])) test case