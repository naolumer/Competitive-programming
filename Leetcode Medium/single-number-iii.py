import collections
class Solution:
    def singleNumber(self, nums):
        count = collections.Counter(nums)
        arr = []
        for c,f in count.items():
            if f==1:
                arr.append(c)
        return arr
