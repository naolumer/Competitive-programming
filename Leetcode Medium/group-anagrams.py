from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
     
        hashMap = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord("a")]+=1
            
            hashMap[tuple(count)].append(s)
            
        return hashMap.values()