# Write a Python Program to Find LCM
x= int(input())
y = int(input())
if x>y:
    greater = x
else:
    greater = y
while(True):
    if(greater%x == 0) and (greater%y == 0):
        lcm = greater
        break
    greater = greater+1
print(greater)

# output:- 
# 3
# 5
# 15
