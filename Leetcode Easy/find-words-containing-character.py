class Solution(object):
    def findWordsContaining(self, words, x):
        return [i for i in range(len(words)) if x in words[i]]