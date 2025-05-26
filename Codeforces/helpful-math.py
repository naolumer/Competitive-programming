s= input()
 
if len(s)==1:
    print(s)
else:
    d= s.split("+")

    ol=[]
    tl=[]
    thrl=[]
    for num in d:
        if num=="1":
            ol.append(num)
    for num in d:
        if num=="2":
            tl.append(num)
    for num in d:
        if num=="3":
            thrl.append(num)
            
    fl= ol+tl+thrl
    ffl= "+".join(fl)
    print(ffl)