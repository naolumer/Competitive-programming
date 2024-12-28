if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    sortted = sorted(set(arr))
    
    print(sortted[-2])