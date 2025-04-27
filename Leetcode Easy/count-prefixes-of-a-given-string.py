
def countPrefixes(self, words, s):

        finalAnswer= 0
        for i in range(len(words)):
            if s.startswith(words[i]):
                finalAnswer+=1
        return finalAnswer