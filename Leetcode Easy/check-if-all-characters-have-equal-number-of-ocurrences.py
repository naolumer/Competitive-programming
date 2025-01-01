from collections import Counter
class Solution(object):
    def areOccurrencesEqual(self, s):
       
        count = Counter(s)
        cur = count(s[0])
        for i in range(len(s)):
            if count[s[i]]!=cur:
                return False
        return True
            