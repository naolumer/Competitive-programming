def strStr(haystack, needle):

    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            if needle == haystack[i:i+len(needle)]:
                return i
    return -1
        