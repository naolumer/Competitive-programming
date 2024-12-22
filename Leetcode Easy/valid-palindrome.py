def isPalindrome(self, x):
    s_num=str(x)
    counter= len(s_num)

    rev_num=""
    for i in range(len(s_num)):
        counter-=1
        reverse_num= s_num[counter]
        rev_num+=reverse_num
    
    
    return rev_num==s_num