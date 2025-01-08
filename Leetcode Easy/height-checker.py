class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortted = sorted(heights)
        print(sortted)
        count = 0
        for i in range(len(heights)):
            if not heights[i]==sortted[i]:
                count+=1
        return count