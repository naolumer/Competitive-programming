class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums1 = sorted(nums[:])
        xor = 0
        
        for i in range(1,len(nums1)):
            if nums1[i]^nums1[i-1]==0:
                return nums1[i]
