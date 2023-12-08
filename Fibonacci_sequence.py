# Write a Python Program to Print the Fibonacci sequence.
num = int(input())
start1, start2 = 0, 1
count = 0
while count < num:
    print(start1)
    temp = start1 + start2
    start1 = start2
    start2 = temp
    count  = count+1

output:-
0
1
1
2
3
5
8
13
