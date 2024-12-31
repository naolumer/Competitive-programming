class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        unique_sort = sorted(set(arr))

        dc = {num:index +1 for index,num in enumerate(unique_sort)}
        answer_arr = []
        for num in arr:
            answer_arr.append(dc[num])
        return answer_arr