from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s)<3:
            return len(s)
        res = 0
        count = Counter(s)
        n = len(s)
        for char,frq in count.items():
            if frq >=3 and frq%2!=0:
                n-= frq-1
            if frq>=3 and frq%2==0:
                n-= frq-2
        return n