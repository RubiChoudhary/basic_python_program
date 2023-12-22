num = "rubi"
reverse = ""
for i in range(len(num)-1,-1,-1):
    reverse = reverse + num[i]
print(reverse)

for i in range(len(num) - 1, -1, -1):
    reverse = reverse + num[i]

if reverse == num:
    print(True)
else:
    print(False)
