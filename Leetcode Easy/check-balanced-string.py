class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        sumodd= 0
        sumeven =0
        for i in range(len(num)):

            if i%2==0:
                sumeven+= int(num[i])
            if i%2!=0:
                sumodd+=int(num[i])
        return sumodd == sumeven