from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count  = Counter(arr)
        seen = {}
        for num,occ in count.items():
            if occ in seen:
                return False
            else:
                seen[occ] = 1
        return True