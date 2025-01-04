class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sortted = sorted(set(nums))
        print(sortted)

        if len(sortted)< 3:
            return sortted[-1]
        else:
            return sortted[-3]