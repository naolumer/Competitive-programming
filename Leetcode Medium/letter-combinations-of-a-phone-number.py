class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        sol = []
        ans = []
        n = len(digits)
        if not digits:
            return []
        
        letter_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        def backtrack(i):
            if i == n :
                ans.append("".join(sol))
                return
            
            for char in letter_map[digits[i]]:

                sol.append(char)
                backtrack(i+1)
                sol.pop()
        
        backtrack(0)
        return ans