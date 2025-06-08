#  Square root calculator without using built-in functions
#  using binary search algorithms
def sqrtt(x):
    low,high = 0, x//2 + 1

    while low<=high:
        
        if x==1 or x==0:
            return x
        mid = (high + low)//2

        if mid*mid == x:
            return x
        elif mid*mid<x:
            low = mid + 1
        elif mid*mid >x:
            high = mid-1
    return high


    

