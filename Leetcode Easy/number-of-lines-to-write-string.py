class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        tot=0
        lines=1
        for i in s:
            if tot+widths[ord(i)-97]>100:
                tot=0
                lines+=1
            tot+=widths[ord(i)-97]
        return [lines,tot] 