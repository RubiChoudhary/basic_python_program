# Write a Python Program to Make a Simple Calculator with 4 basic mathematical
# operations.
print(""" Select operations.:
            1 for Add
            2 for substract
            3 for multiply
            4 for divide""")
choice = int(input("Select 1 to 4: "))
num1=int(input("Enter the num: "))
num2=int(input("Enter the num: "))
if choice == 1:
    sum1 = num1+num2
    print("Your addition is : ",sum1)
elif choice == 2:
    substract = num1 - num2
    print("Your substraction is : ",substract)
elif choice == 3:
    multiplication = num1 * num2
    print("Your multiplication is : ",multiplication)
else:
    division = num1 / num2
    print("Your division is : ",division)
