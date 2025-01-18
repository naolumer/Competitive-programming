class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = 0
        double = 0

        for num in nums:
            if len(str(num)) ==2:
                double += int(num)
            else:
                single+=num
        return single!=double