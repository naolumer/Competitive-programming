from collections import Counter
def majorityElement(nums):
    # n= len(nums)
    # majority = n/2

    # appearanceDic={}

    # for num in nums:
    #     if num in appearanceDic:
    #         appearanceDic[num]+=1
    #     else:
    #         appearanceDic[num]=1
    
    # for num in appearanceDic:
    #     if appearanceDic[num] > majority:
    #         return num

# test case 👇
# print(majorityElement([3,2,3,2,2]))  

    # BETTER SOLUTION;

    count = Counter(nums)
    n = len(nums)

    for key,freq in count.items():
        if freq > n/2:
            return key


