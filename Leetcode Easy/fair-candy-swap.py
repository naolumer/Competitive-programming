class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
   
        sum_A, sum_B = sum(aliceSizes), sum(bobSizes) 
        bob_set = set(bobSizes)

        delta = (sum_A - sum_B) // 2
        for a in aliceSizes:
            b = a - delta
            if b in bob_set:
                return [a, b]

        return []
        