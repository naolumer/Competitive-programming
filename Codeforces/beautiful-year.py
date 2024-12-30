y= int(input())
 
for i in range(y+1,10000):
    sb={}
    for char in str(i):
        if char in sb:
            sb[char]+=1
        else:
            sb[char]=1
    if len(sb)==len(str(i)):
        print(i)
        break