from collections import Counter
from types import List

class Solution:
    
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        count = Counter(nums)
        arr= []
        for num,frq in count.items():
            if frq==2:
                arr.append(num)
        return arr