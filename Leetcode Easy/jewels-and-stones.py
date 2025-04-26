from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count_s = Counter(stones)
        ans = 0
        for char,count in count_s.items():
            if char in jewels:
                ans+=count
        return ans