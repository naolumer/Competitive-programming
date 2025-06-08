def isPalindrome(self, x):
    s_num=str(x)
    counter= len(s_num)

    rev_num=""
    for i in range(len(s_num)):
        counter-=1
        reverse_num= s_num[counter]
        rev_num+=reverse_num
    
    
    return rev_num==s_num

#  Alternative two-pointer solution

    # x.strip()
    # s = [char for char in x if char.isalnum()]
    # sl =  [char.lower() for char in s]

    # l  = 0
    # r = len(sl)-1

    # while l<=r:
    #     if sl[l]==sl[r]:
    #         l+=1
    #         r-=1
    #     else:
    #         return False
    # return True