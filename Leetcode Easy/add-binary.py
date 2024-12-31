class Solution(object):
    def addBinary(self, a, b):
       
        int_a= int(a,2)
        int_b=int(b,2)

        sum_int= int_a + int_b
        sum_bin= bin(sum_int)[2:]

        return sum_bin