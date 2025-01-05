class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left,right+1):
            n = str(i)
            if all(int(j) != 0 and i % int(j) == 0 for j in n):
                ans.append(i)
        return ans