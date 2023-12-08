# Write a Python Program to Find the Factorial of a Number.
num = int(input())
factorial = 1
if num ==0:
  print("Facotrial for 0 is 1")
else:
  for i in range(1, num+1):
    factorial = factorial *i
  print(f'the factorial of {num} is {factorial}')
