row  = 3
column= 5
matrix = []
sum = 0
for i in range(row):
    temp = []
    for j in range(column):
        sum = i+j
        temp.append(sum)
    matrix.append(temp)
print(matrix)