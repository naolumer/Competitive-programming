class Solution:
    def findNumbers(self, nums):
        def helper(num):
            strnum  =str(num)
            n = len(strnum)
            return n
        count = 0
        for num in nums:
            if helper(num)%2==0:
                count+=1
        return count