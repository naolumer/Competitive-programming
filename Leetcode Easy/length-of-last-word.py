class Solution(object):
    def lengthOfLastWord(self, s):
      
        wospace = s.strip()
        lis = wospace.split(" ")
        return len(lis[-1])