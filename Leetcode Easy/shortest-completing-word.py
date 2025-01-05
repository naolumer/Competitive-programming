from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        countlp = Counter(char.lower() for char in licensePlate if char.isalpha())
        def helper(word):   # check whether or not a word has all letters in licensePlate
            
            countw  = Counter(word)
            for key,val in countlp.items():
                if countw[key]<val:
                    return False
            return True
        
        sortted_words = sorted(words,key=len)
        
        for word in sortted_words:
            if helper(word):
                return word
        return "" 