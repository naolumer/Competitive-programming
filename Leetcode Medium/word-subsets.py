from collections import defaultdict,Counter
class Solution:
    def wordSubsets(self, words1,words2):
        count_c = defaultdict(int)

        for w in words2:
            countw = Counter(w)
            for char,count in countw.items():
                count_c[char] = max(count_c[char],count)
        
        
        ans = []
        for w in words1:
            countw = Counter(w)
            flag = True
            for char,count in count_c.items():
                if countw[char] < count:
                    flag = False
                    break
            if flag:
                ans.append(w)
        return ans
