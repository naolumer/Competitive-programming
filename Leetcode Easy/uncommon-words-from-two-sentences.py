def uncommonFromSentences(s1, s2):
        
    split1= s1.split()
    split2= s2.split()
    

    seen_dic1= {}
    seen_dic2= {}

    for word in split1:
        if word in seen_dic1:
            seen_dic1[word]+=1
        else:
            seen_dic1[word]=1

    for word in split2:
        if word in seen_dic2:
            seen_dic2[word]+=1
        else:
            seen_dic2[word]=1
    answer=[]
    for key in seen_dic1:
        if seen_dic1[key]==1 and key not in split2:
            answer.append(key)
    
    for key in seen_dic2:
        if seen_dic2[key]==1 and key not in split1:
            answer.append(key)
    return answer