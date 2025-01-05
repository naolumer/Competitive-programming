class Solution:
    def toLowerCase(self, s: str) -> str:
        new_s = ""
        for char in s:
            char = char.lower()
            new_s+=char
        return new_s