class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        l = [num for num in binary]
        for i in range(len(l)):
            if l[i]=="0":
                l[i]="1"
            elif l[i]=="1":
                l[i]="0"
        return int("".join(l),2)