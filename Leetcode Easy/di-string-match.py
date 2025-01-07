class Solution:
    def diStringMatch(self, s: str) -> List[int]:

        # two pointers solution (O(n))
        
        ans = []
        i = 0
        d = len(s)
        
        for char in s:
            if char == "I":
                ans.append(i)
                i+=1
            else:
                ans.append(d)
                d-=1
        ans.append(sum(range(0,len(s)+1))-sum(ans))