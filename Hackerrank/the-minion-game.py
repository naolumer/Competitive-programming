def minion_game(string):
    vowels = "AEIOU"
    length = len(string)
    StuartVal,KevinVal = 0,0
    for i in range(length):
        if string[i] in vowels:
            KevinVal += length-i
        else:
            StuartVal += length-i
    
    
    if StuartVal == KevinVal:
        print("Draw")
    elif StuartVal > KevinVal:
        print("Stuart"+" "+str(StuartVal)) 
    else:
        print("Kevin"+" "+str(KevinVal))      
            
    # your code goes here

if __name__ == '__main__':
    s = input()
    minion_game(s)