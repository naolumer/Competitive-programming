class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_str = ""
        sum_len = len(word1) +  len(word2)
        
        w1p = 0
        w2p = 0

        for i in range(sum_len):
            if not w1p> len(word1)-1:
                new_str+=word1[i]
                w1p+=1
            
            if not w2p> len(word2)-1:
                new_str+=word2[i]
                w2p+=1
        return new_str