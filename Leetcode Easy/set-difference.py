# Solution to the set diffence problem in hackerrank
n = int(input())
english = set(input().split())
m = int(input())
french = set(input().split())

print(len(english.difference(french)))

    