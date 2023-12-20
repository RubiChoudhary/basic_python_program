bubble = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
n = len(bubble)
for i in range(n):
    for j in range(0, n - i - 1):
        if bubble[j] > bubble[j + 1]:
            bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]
print("Bubble Sort:", bubble)
