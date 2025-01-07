from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        count = Counter(words[0])
        for word in words[1:]:
            cur_count = Counter(word)
            for c in count:
                count[c] = min(count[c],cur_count[c])
        answer = []
        for key,val in count.items():
            for i in range(val):
                answer.append(key)
        return answer