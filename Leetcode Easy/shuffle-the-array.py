from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        half_num1 = nums[:n]
        half_num2= nums[n:]

        new_arr = []
        for i in range(n):
            new_arr.append(half_num1[i])
            new_arr.append(half_num2[i])
        
        return new_arr