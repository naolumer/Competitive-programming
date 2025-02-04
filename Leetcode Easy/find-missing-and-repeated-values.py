from collections import Counter
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        full_array = []
        for i in range(len(grid)):
            for j in range(len(grid)):
                full_array.append(grid[i][j])
        
        count = Counter(full_array)
        ans = []
        n = len(grid)
        for num,frq in count.items():
            if frq==2:
                ans.append(num)
        for i in range(1,(n*n)+1):
            if not i in full_array:
                ans.append(i)
        return ans