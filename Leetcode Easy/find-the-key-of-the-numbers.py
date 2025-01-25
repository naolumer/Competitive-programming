class Solution(object):
    def generateKey(self, num1, num2, num3):
        """
        :type num1: int
        :type num2: int
        :type num3: int
        :rtype: int
        """
        n1 = (str(num1))
        n2 = (str(num2))
        n3 = (str(num3))
        
        res = ""
        if len(n1)<4:
            for i in range(4-len(n1)):
                res+="0"
            n1 = res+n1
        res3=""
        if len(n3)<4:
            for i in range(4-len(n3)):
                res3+="0"
            n3 = res3+n3
        res2 = ""
        if len(n2)<4:
            for i in range(4-len(n2)):
                res2+="0"
            n2 = res2+n2
        
        dig = ""

        dig+= min(n1[0],n2[0],n3[0])
        dig+= min(n1[1],n2[1],n3[1])
        dig+= min(n1[2],n2[2],n3[2])
        dig+= min(n1[3],n2[3],n3[3])

        dd = list(str(dig))

        for i in range(4):
            if dd[i] =="0":
                continue
            else:
                return int("".join(dd[i:]))
        return 0