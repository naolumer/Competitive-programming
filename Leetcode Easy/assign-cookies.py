
def assignCookies(g,s):

    g.sort()
    s.sort()

    contentChildren = 0
    cookieIndex = 0

    while cookieIndex < len(s) and contentChildren < len(g):

        if s[cookieIndex] >= g[contentChildren]:
            contentChildren+=1
        cookieIndex+=1
    return contentChildren
    
print(assignCookies([1,2],[1,2,3]))


