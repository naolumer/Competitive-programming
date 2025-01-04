class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pts,stp = {},{}

        sl = s.split(" ")
        
        if len(pattern)!=len(sl):
            return False
        
        for i in range(len(pattern)):
            p,s = pattern[i],sl[i]

            if (p in pts and pts[p]!=s) or (s in stp and stp[s]!=p):
                return False
            pts[p] = s
            stp[s] = p
        return True