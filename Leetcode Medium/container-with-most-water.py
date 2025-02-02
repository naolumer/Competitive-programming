class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l= 0
        r = len(height)-1
        max_area = 0

        while r>l:
            area = min(height[r],height[l]) * (r-l)
            max_area = max(area,max_area)

            if height[r]>=height[l]:
                l+=1
            else:
                r-=1
        return max_area