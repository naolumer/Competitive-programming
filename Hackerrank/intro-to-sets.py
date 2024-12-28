def average(array):
    
    set_ = sorted(set(array))
    
    summ = sum(set_)
    ave = round(summ/len(set_),3)
    return ave
        
        
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)