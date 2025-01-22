class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        p1 = len(nums)-1
        p2 = 0

        arr = nums[:]
        for n in nums:
            if n%2==0:
                arr[p2] = n
                p2+=1
            else:
                arr[p1] = n
                p1-=1
        return arr