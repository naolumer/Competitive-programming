n= int(input())
lis=[]
for i in range(n):
    nums= list(map(int, input().split() ))
    lis.append(nums)
tl=[]
for ab in lis:
    tl.append(ab[1]-ab[0])
sl=[tl[0]]
for i in range(1,n):
    tl[i]=tl[i]+ tl[i-1]
    sl.append(tl[i])
print(max(sl))