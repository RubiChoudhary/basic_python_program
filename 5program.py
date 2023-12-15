# Factorial
n = int(input("enter the number: "))
if n < 0:
    print("Factorial is not defined for negative numbers.")
elif n == 0 or n == 1:
    print(1)
else:
    result = 1
    for i in range(2, n + 1):
        result = result * i
    print(result)



# palindrome
palindrome = str(input("enter the palindrome string: "))
if palindrome == palindrome[::-1]:
    print(f"{palindrome} is palindrome")
else:
    print(f'{palindrome} is not a palindrome')


# prime number
number = int(input("enter the number: "))
if number <= 1:
    print("negative prime number doesn't exist")
else:
    for i in range(2, number):
        if number % i == 0:
            print("not a prime number")
    print("prime number ", number)


# fizzbuzz
for i in range(1, 25):
    if i % 3 == 0:
        print("fizz", end = " " )
    elif i % 5 == 0:
        print("buzz", end = " ")
    elif (i % 3 == 0) and (i % 5 == 0):
        print("fizzbuzz", end = " ")
    else:
        print(i, end = " ")


num = input("enter the palindrome number: ")
temp = num
reverse_num = 0
while temp != 0:
   digit = temp % 10
   reverse_num = (reverse_num * 10) + digit
   temp = temp // 10
if num == reverse_num:
   print(num, "is a palindrome number")
else:
   print(num, "is not a palindrome number")




# fibonacci
num = int(input("enter the number: "))
if num == 1:
    print(1)
elif num == 0:
    print(1)
else:
    print(1, 1, end=" ")
    a = 1
    b = 1
    for i in range(2, num+1):
        c = a+b
        print(c, end=" ")
        a = b
        b = c