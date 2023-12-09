# Write a Python Program to Find Armstrong Number in an Interval.
start = 10
end = 1000
for i in range(start, end+1):
    power = len(str(i))
    num = i
    sum1 =0
    
    while num>0:
        digit = num%10
        sum1= sum1+digit**power
        num = num//10
    if i == sum1:
        print(i)
