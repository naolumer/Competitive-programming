from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
     
        hashmap = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord("a")]+=1
            
            hashmap[tuple(count)].append(s)
            
        return hashmap.values()