
def licenseKeyFormatting( s, k):
       
    s.split("-")
    wor="".join(s.split("-"))
    word= wor.upper()
    

    keri= len(word)%k
    first= word[:keri]
    rest= word[keri:]

    solution= [first]
    i=0
    if len(word)%k!=0:
        while i<len(rest):
            cutt= rest[i:i+k]
            if cutt!="":
                solution.append(cutt)
            i+=k
        return "-".join(solution)

    elif len(word)%k==0:
        solution.remove(first)
        while i<len(word):
            cutt= word[i:i+k]
            if cutt!="":
                
                solution.append(cutt)
            i+=k
        return "-".join(solution)