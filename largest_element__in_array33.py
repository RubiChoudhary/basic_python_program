# Write a Python Program to find largest element in an array
arr_str = input()
arr = []

for x in arr_str.split():
    arr.append(int(x))

n = len(arr)

max_element = arr[0]

for i in range(1, n):
    if arr[i] > max_element:
        max_element = arr[i]

print("largest element is", max_element)
