# Write a Python Program for array rotation.
arr = [1, 2, 3, 4, 5]
d = 2
n = len(arr)

if d < 0 or d >= n:
    print("Invalid rotation value")
else:
    rotated_arr = [0] * n

    for i in range(n):
        rotated_arr[i] = arr[(i + d) % n]

    print("Original Array:", arr)
    print("Rotated Array:", rotated_arr)
