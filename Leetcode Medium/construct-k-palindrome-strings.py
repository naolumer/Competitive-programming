from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        count_of_chars = Counter(s)
        if len(s)<k:
            return False
        odd_count = 0

        for count in count_of_chars.values():
            if count%2!=0:
                odd_count+=1
        return odd_count <= k