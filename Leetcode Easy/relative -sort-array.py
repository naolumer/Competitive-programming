from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        countarr1 = Counter(arr1)
        temp = []
        temp2=[]
        
        for char in arr2:
            for i in range(countarr1[char]):
                temp.append(char)
                countarr1[char] = 0
        for char,frq in countarr1.items():
            for i in range(frq):
                temp2.append(char) 

        for char in sorted(temp2):
            temp.append(char)
        
        return temp