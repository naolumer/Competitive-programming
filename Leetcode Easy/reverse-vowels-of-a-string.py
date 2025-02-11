class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s)== 0 or len(s)==1:
            return s
        vowels = ['a', 'e', 'i', 'o','u']
        sl = list(s)
        r = len(sl)-1
        l = 0
        while l<r:
            if sl[r].lower() not in vowels:
                r-=1
            if sl[l].lower() not in vowels:
                l+=1
            if (sl[l].lower() in vowels) and (sl[r].lower() in vowels):
                sl[l],sl[r] = sl[r],sl[l]
                l+=1
                r-=1
        res = ""
        for char in sl:
            res+=char
        
        return res