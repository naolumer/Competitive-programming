def isValid(self, s):

        brackets={")":"(","]":"[","}":"{"}
        stack=[]
        
        for c in s:
            if c in brackets:
                if stack and stack[-1]==brackets[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack)==0