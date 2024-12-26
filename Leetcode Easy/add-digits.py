def addDigits(self, num: int) -> int:

    #   Solution 1. Recursive
    # while num>9:
    #     num = int(num%10) + self.addDigits(int(num/10))
      
    # return num

    # Solution 2. While Lopp

    # while num > 9:
    #     num = int(num%10) + int(num/10)
    # return num

    # Solution 3. Math

    # return 0 if num ==0 else (num-1)%9 + 1

