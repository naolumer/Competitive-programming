def RomanToInt(s):


    roman_dic = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }

    m = len(s)
    i=0
    result = 0

    while i< m :
        curr_value = roman_dic[s[i]]

        if i<m-1 and curr_value < roman_dic[s[i+1]]:
            result-= curr_value
        else:
            result +=curr_value
        i+=1
    return result
print(RomanToInt("XXX"))


