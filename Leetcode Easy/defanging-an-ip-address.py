class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ""
        for char in address:
            if char==".":
                ans+="[.]"
            else:
                ans+=char
        return ans