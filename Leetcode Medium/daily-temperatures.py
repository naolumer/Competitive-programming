class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        t = temperatures
        n = len(t)
        ans = [0]*n
        stack = []    # initialize our stack

        for i,temp in enumerate(t):
            while stack and stack[-1][0] < temp:
                stack_t,stack_i = stack.pop()
                ans[stack_i] = i - stack_i
            stack.append((temp,i))
        
        return ans