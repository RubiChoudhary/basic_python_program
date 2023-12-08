num = int(input("Enter a number: "))

if num == 1:
    print("Not a prime number:", num)
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("Not a prime number:", num)
            break
    else:
        print("Is a prime number:", num)
