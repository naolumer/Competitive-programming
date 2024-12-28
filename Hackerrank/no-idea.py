# Read the first line containing n and m
n, m = map(int, input().split())

# Read the array of integers
array = list(map(int, input().split()))

# Read the integers in set A
set_a = set(map(int, input().split()))

# Read the integers in set B
set_b = set(map(int, input().split()))
happy=0

for i in range(n):
    if array[i] in set_a:
        happy+=1
    elif array[i] in set_b:
        happy-=1
    else:
        continue
print(happy)