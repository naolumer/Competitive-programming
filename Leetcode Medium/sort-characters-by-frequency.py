def frequencySort(s):
        
    dicc={}
    for char in s:
                if char in dicc:
                    dicc[char]+=1
                else:
                    dicc[char]=1
    sortd= sorted(dicc.items(), key= lambda item: item[1], reverse=True)
    
    f_str=""
    for char,count in sortd:
        
        f_str+= char*count
            
    return f_str