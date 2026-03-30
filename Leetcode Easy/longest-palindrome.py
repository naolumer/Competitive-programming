class Solution(object):
    
    def longestPalindrome(self, s):
        
        seenDict = {}

        for letter in s:
            if letter in seenDict:
                seenDict[letter] +=1
            else:
                seenDict[letter] = 1
        
        palindromeLength = 0
        has_odd = False

        for key in seenDict:
            if seenDict[key]%2==0:
                palindromeLength += seenDict[key]
            else:
                palindromeLength += seenDict[key]-1
                has_odd = True
        if has_odd:
            return palindromeLength+1
        else:
            return palindromeLength
