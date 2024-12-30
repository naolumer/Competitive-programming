from sys import stdin
def input(): return stdin.readline().strip()
from collections import Counter
 
for _ in range(int(input())):
    n,m = [int(i) for i in input().split()]
    problems = input()
    lettlist=["A","B","C","D","E","F","G"]
    dicc={ch:0 for ch in lettlist}
 
 
    solution = 0
 
    for lett in problems:
        dicc[lett] += 1
 
 
    for lett in lettlist:
        if dicc[lett] < m:
            solution += (m - dicc[lett])
        
    print(solution)