class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
 
        paragraph = paragraph.replace(",", " ").lower()
        paragraph = "".join(char for char in paragraph if char.isalpha() or char == " ")
        paragraph = paragraph.split(" ")

        wordict = {}

        for word in paragraph:
            if word not in banned and word != "":
                if word in wordict:
                    wordict[word] += 1
                else:
                    wordict[word] = 1
                    
        return max(wordict, key=wordict.get)