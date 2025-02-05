from collections import Counter
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        res1 = 0
        for char,frq in count1.items():
            if char in count2:
                res1+=frq
        res2 = 0
        for char,frq in count2.items():
            if char in count1:
                res2+=frq
        return [res1,res2]