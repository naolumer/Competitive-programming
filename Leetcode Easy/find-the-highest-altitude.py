class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res =[0,gain[0]]

        for i in range(1,len(gain)):
            res.append(sum(gain[:i+1]))
        
        return max(res)