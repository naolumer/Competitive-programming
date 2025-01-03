class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        doubled_s = s + s
        new_s  = doubled_s[1:-1]

        return s in new_s