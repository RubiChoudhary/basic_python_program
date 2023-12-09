# Write a Python Program for cube sum of first n natural numbers?
n = int(input("enter the number: "))
total = 0
if n<=0:
    print("negative numbers doesn't exist")
else:
    for i in range(1, n+1):
        total = total + i**3
        print(total, end = ' ')
