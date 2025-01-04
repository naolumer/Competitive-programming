from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        counts = Counter(s)
        countt = Counter(t)

        for key,val in countt.items():
            if not key in counts or val > counts[key]:
                return key