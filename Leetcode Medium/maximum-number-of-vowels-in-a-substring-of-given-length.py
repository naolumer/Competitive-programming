class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = "aeiou"
        n = len(s)

        cur_count = 0

        for i in range(k):
            if s[i] in vowels:
                cur_count+=1
        
        max_count = cur_count

        for i in range(k,n):
            if s[i] in vowels:
                cur_count+=1
            if s[i-k] in vowels:
                cur_count-=1
            
            count = cur_count
            max_count = max(count,max_count)
        
        return max_count