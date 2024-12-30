def solution(word):
    length= len(word)
    if length<=10:
        new_word=word
 
    else:
        first_letter= word[0]
        last_letter= word[length-1]
        middle_num= length-2
        new_word=first_letter+str(middle_num)+last_letter
        
    return new_word
 
n = int(input())
for i in range(n):
    x = input()
    print(solution(x))