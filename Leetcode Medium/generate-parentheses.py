class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:

        stack,result = [],[]

        def backtrack(o,c):

            if len(stack)==n*2:
                result.append("".join(stack))
                return
            
            if o < n:
                stack.append("(")
                backtrack(o+1,c)
                stack.pop()
            
            if c < o:
                stack.append(")")
                backtrack(o,c+1)
                stack.pop()

        backtrack(0,0)
        return result