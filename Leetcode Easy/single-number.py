from collections import Counter
def singleNumber( nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dicc= {}
        
        # counter= len(nums)
        # for num in nums:
        #     if num in dicc:
        #         dicc[num]+=1
        #     else:
        #         dicc[num]=1
                    
        # for keys in dicc:
        #     if dicc[keys]!=2:
        #         n= keys
        # return n

        # Using hashmaps

        count = Counter(nums)
        for key,count in count.items():
              if count == 1:
                    return key
        
        
        
        
        
        # More efficient solution using XOR


        unique = 0
        for num in nums:
            unique^=num      # XOR each number with the current unique value
        return unique