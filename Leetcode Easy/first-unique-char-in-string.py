from collections import Counter
def firstUniqChar(s: str) -> int:
    count = Counter(s)

    for char,frq in count.items():
        if frq==1:
            return s.index(char)
    return -1