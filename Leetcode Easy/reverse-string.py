def reverseString(s):

    last_pointer = len(s)-1
    i = 0
    while i<=last_pointer:
        s[i],s[last_pointer]=s[last_pointer],s[i]
        last_pointer-=1
        i+=1