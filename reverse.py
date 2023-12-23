numbers = [34,6,8,3,6,9,78]
for num in numbers:
        print(num, end=' ')

for num in range(len(numbers)-1, -1, -1):
    print(num, end=' ')

for num in range(len(numbers)-1, -1, -1):
    x = numbers[num]-1
    print(x, end=' ')
