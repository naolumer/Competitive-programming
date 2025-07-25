class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        
        has_vowels = False
        has_constants = False
        
        for c in word:
            if c.isalpha():
                if c.lower() in "aeiou":
                    has_vowels = True
                else:
                    has_constants = True
            elif not c.isdigit():
                return False
        return has_vowels and has_constants

