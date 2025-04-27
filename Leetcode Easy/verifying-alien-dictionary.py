def isAlienSorted(words, order):
       
    orderdic= {c:i for i,c in enumerate(order)}
    words2=[]

    for word in words:
        tmp=[]
        for char in word:
            tmp.append(orderdic[char])
        words2.append(tmp)
    for i in range(1, len(words2)):
        if words2[i]<words2[i-1]:
            return False
    
    return True