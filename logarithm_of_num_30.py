# Write a Python Program to calculate the natural logarithm of any number.
import math 
num = float(input("enter the number: "))
if num<=0:
    print("enter the poistive number")
else:
    result = math.log(num)
    print("log is ", result)
