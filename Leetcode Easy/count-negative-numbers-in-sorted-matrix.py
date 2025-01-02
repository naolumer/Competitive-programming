class Solution(object):
    def countNegatives(self, grid):
        
        count = 0
        for num in grid:
            for g in num:
                if g<0:
                    count+=1

        return count