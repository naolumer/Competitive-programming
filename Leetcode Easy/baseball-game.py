class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []

        for char in operations:
            if  char =='+':
                if len(ans)>=2:
                    ans.append(int(ans[-1])+int(ans[-2]))
            elif char =="C":
                ans.pop()
            elif char =="D":
                if ans:
                    ans.append(int(ans[-1])*2)
            else:
                ans.append(int(char))

        return sum(ans)