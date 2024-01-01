a1 = input("enter the number: ").split()
n = len(a1)
a = list(map(int, a1))
unique_list = []
duplicate_list = []
for i in a:
    if i not in unique_list:
        unique_list.append(i)
    elif i not in duplicate_list:
        duplicate_list.append(i)
print(unique_list)
print(duplicate_list)
