# stack data-structure is used to solve this problem


from collections import deque  # helps us to create a deque list that will enable us to quickly get the rightmost and left most element from a list

t = int(input())

while t > 0 :

    n = int(input())
    l = list(map(int , input().split()))
    lst = deque(l)
    
    rm =  lst.pop()
    lm =  lst.popleft
    csv = max(rm , lm)
    flag= False

    while len(lst) > 0 :

        if lm>=rm and lm<=csv:
            csv =lm
            lm = lst.popleft()
            latest = lm
        
        elif rm>lm and rm<=csv:
            csv =rm          # update csv to the rightmost cube
            rm = lst.pop()   # pick the next rightmost element
            latest = rm      # update latest to rightmost element
        
        else:
            flag = True # we cannot pick a valid cube
            break
    
    # check if the last picked cubesize is valid
    
    if flag or latest > csv: 
        print('No')
    else:
        print('Yes')
            
    t-=1   # move to the next testcase