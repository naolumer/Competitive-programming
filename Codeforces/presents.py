n= int(input())
number= input().split()
 
 
 
nums= [int(num) for num in number]
ff=[]
for i in range(len(nums)+1):
    if i in nums:
        ff.append(str(nums.index(i)+1))
        
print(" ".join(ff))