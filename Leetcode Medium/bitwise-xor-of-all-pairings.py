class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        xor1,xor2 = 0,0

        for num in nums1:
            xor1=xor1^num
        
        for num in nums2:
            xor2 = xor2^num
        
        result = 0

        if len(nums1)%2 ==1:
            result^=xor2
        if len(nums2)%2 ==1:
            result^= xor1
        return result