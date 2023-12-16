a = [1,2,3,4,5,4]
sum = 0
sum1 = 0
for i in a:
    sum1 = sum1+i
print(sum1)
for i in set(a):
    sum = sum+i
print(sum)
if sum != sum1:
    dublicate_number =  sum1 - sum
print("dublicate number is: ", dublicate_number)