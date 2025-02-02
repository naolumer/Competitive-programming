class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        res = 0
        ascii_dict = {char: ord(char) for char in (chr(i) for i in range(65, 91))}    
        ascii_dict.update({char: ord(char) for char in (chr(i) for i in range(97, 123))})  
        l =list(set(word)) 
        new_ascii = {val:key for key,val in ascii_dict.items()}

        for char in l:
            if char.islower():
                if new_ascii[ord(char)-32] in l:
                    res+=1
            if char.isupper():
                if new_ascii[ord(char)+32] in l:
                    res+=1