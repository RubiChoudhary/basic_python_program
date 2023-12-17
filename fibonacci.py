num= int(input("enter the number: "))
if num == 1:
    print(1)
elif num == 0:
    print(1)
else:
    print(1,1, end=" ")
    a = 1
    b = 1
    for i in range(2,num):
        c= a+b
        print(c, end=" ")
        a=b
        b=c
