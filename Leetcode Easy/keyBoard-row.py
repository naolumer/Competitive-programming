def findWords( words):
        
    str1 = "qwertyuiop"
    str2 = "asdfghjkl"
    str3 = "zxcvbnm"

    strl1 = [char for char in str1]
    strl2 = [char for char in str2]
    strl3 = [char for char in str3]
    
    answer = []
    
    for word in words:
        if all(x.lower() in strl1 for x in word):
            answer.append(word)
        elif all(x.lower() in strl2 for x in word):
            answer.append(word)
        elif all(x.lower() in strl3 for x in word):
            answer.append(word)
    return answer