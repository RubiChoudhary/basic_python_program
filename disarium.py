# A Disarium number is a number that is equal to the sum of its digits each raised to the
# power of its respective position. For example, 89 is a Disarium number because
# 8^1 + 9^2= 8 + 81 = 89.
num = int(input("Enter a number: "))
num_str = str(num)
sum = 0
for i in range(len(num_str)):
    sum = sum + int(num_str[i]) ** (i + 1)
    print(sum)
if sum == num:
    print(f"{num} is a Disarium number.")
else:
    print(f"{num} is not a Disarium number.")