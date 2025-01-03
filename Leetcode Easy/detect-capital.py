class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if all(char.islower() for char in word):
            return True
        if all(char.isupper() for char in word):
            return True
        if word[0].isupper():
            if all(char.islower() for char in word[1:]):
                return True
        return False