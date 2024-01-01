n = int(input("Enter the size of array a: "))
a = list(map(int, input("Enter the elements of array a separated by space: ").split()))
m = int(input("Enter the size of array b: "))
b = list(map(int, input("Enter the elements of array b separated by space: ").split()))

# Creating an empty set to store unique elements
union_set = set()
count = 0
for i in range(n):
    if a[i] not in union_set:
        union_set.add(a[i])
        count += 1
for i in range(m):
    if b[i] not in union_set:
        union_set.add(b[i])
        count += 1
print("Count of elements in the union:", count)
