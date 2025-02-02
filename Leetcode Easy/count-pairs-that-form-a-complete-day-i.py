class Solution(object):
    def countCompleteDayPairs(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(hours)):
            for j in range(i+1,len(hours)):
                if (hours[i]+hours[j])%24==0:
                    res+=1
        return res