class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        arr = []
        n=len(nums)
        for i in range(int(n/2)):
            mi = min(nums)
            ma = max(nums)
            nums.pop(nums.index(mi))
            nums.pop(nums.index(ma))
            arr.append((float(mi+ma)/2))
        return min(arr)