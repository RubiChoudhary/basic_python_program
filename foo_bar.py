num = int(input("enter the number: "))
if (num%5 == 0) and (num%7 == 0):
    print("foobar")
elif num%5 ==0:
    print("foo")
elif num%7 == 0:
    print("bar")
else:
    print("cannot be divisible by 5 and 7")

