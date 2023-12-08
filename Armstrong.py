# Write a Python Program to Check Armstrong Number?
num = int(input("enter number:"))
num_str = str(num)
num_digits = len(num_str)
sum_of_powers = 0
temp_num = num
while temp_num > 0:
    digit = temp_num % 10
    sum_of_powers += digit ** num_digits
    temp_num //= 10
if sum_of_powers == num:
    print("Armstrong number.", num)
else:
    print("not an Armstrong number.", num)

output:-
153 
1^3 + 5^3 + 3^3 
1 + 125 + 27 = 153
