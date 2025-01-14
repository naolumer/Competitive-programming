from collections import Counter
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        for i in range(len(A)):
            cA,cB = Counter(A[:i+1]),Counter(B[:i+1])
            ans = 0
            for char in A[:i+1]:
                if cA[char] + cB[char]==2:
                    ans+=1
            res.append(ans)
        return res