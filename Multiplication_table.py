# Write a Python Program to Display the multiplication Table.
num = int(input())
for i in range(1,11):
    multiplication = num*i
    result = "{} * {}  = {}".format(num,i, multiplication)
    print(result)
