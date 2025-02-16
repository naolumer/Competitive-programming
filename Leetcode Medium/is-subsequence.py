class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)

        if s =="" : return True
        if len_s > len_t: return False
        j=0
        for i in range(len_t):
            if t[i] == s[j]:
                if j == len_s-1:
                    return True
                j+=1
        return False