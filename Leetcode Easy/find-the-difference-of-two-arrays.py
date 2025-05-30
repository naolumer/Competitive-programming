class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        return [[num for num in set1.difference(set2)],[num for num in set2.difference(set1)]]