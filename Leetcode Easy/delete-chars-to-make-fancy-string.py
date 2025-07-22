class Solution(object):
    
    def makeFancyString(self, s):
        
        last = s[0]
        result = s[0]
        count = 1

        if not s:
            return ""

        for i in range(1,len(s)):

            if s[i] != last:
                last = s[i]
                count = 0
            count +=1

            if count > 2:
                continue
            result += s[i]

        return result
            
        