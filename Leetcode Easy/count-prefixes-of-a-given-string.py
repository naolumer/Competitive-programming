
def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        finalAnswer= 0
        for i in range(len(words)):
            if s.startswith(words[i]):
                finalAnswer+=1
        return finalAnswer