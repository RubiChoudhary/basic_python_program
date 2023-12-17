def fibonacci(number):
    a = 1
    b = 1
    list1 = []
    for i in range(number):
        if i<2:
            list1.append(1)
        else:
            c= a+b
            list1.append(c)
            a, b = b, c
    return list1
num = 8
result = fibonacci(num)
print(result)

