class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(1,len(s)):
            res+= abs(ord(s[i-1])-ord(s[i]))
        return res
        