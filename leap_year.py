# Write a Python Program to Check Leap Year.
year=int(input())
if year%4==0 and year%100!=0:
    print("leap year")
elif year%400==0 and year%100==0:
    print("leap year")
else:
    print("not a leap year")
    