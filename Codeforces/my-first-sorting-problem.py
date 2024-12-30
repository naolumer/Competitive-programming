test_cases = int(input())
for i in range(test_cases):
    x,y= map(int, input().split())
    if x>y:
        print(y,x)
    else:
        print(x,y)