n= int(input())
p= input()
sl= p.split()
 
num_array= [float(num) for num in sl]
print(sum(num_array)/n)