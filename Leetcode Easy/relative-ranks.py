from collections import defaultdict
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        sortted = sorted(score,reverse = True)
        dicct = defaultdict()

        for i in range(1,len(sortted)+1):
            dicct[sortted[i-1]] = i
        
        for i in range(len(score)):
            if dicct[score[i]]==1:
                score[i] = "Gold Medal"
            elif dicct[score[i]]==2:
                score[i]="Silver Medal"
            elif dicct[score[i]]==3:
                score[i]="Bronze Medal"
            else:
                score[i] = str(dicct[score[i]])
        return score