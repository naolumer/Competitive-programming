from collections import Counter
class Solution:
    def duplicateNumbersXOR(self, nums) -> int:
        twice = []
        count = Counter(nums)
        for num,frq in count.items():
            if frq==2:
                twice.append(num)
                
        xor = 0

        for num in twice:
            xor=xor^num
        return xor