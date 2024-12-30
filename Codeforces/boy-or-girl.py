string_name= input()
lis=[]
counter=0
for char in string_name:
    if char in lis:
        continue
    else:
        lis.append(char)
        counter+=1
 
if counter%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")