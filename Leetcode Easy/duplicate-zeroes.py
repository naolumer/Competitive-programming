class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        temp = []
        for i in range(len(arr)):
            if len(temp)<len(arr):
                if arr[i]==0:
                    temp.append(arr[i])
                    temp.append(0)
                else:
                    temp.append(arr[i])
        for i in range(len(arr)):
            arr[i]=temp[i]
      