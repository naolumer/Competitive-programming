n = int(input())  
forces = []
 
for _ in range(n):
    force = list(map(int, input().split()))  
    forces.append(force)
 
 
sum_x = sum(force[0] for force in forces)
sum_y = sum(force[1] for force in forces)
sum_z = sum(force[2] for force in forces)
 
if sum_x == 0 and sum_y == 0 and sum_z == 0:
    print("YES")
else:
    print("NO")