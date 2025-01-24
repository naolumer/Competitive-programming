class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        l = [int(num) for num in str(n)]
        n = 1
        for num in l:
            n = n*num
        return n-sum(l) 