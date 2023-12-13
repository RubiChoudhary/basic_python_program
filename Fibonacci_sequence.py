# Write a Python Program to Print the Fibonacci sequence.
n=int(input())
if n ==0:
    print(1)
elif n==1:
    print(1)
else:
    print(1,1, end= ' ')
    a= 1
    b= 1
    for i in range(2, n+1):
        c= a+b
        print(c, end=' ')
        a=b
        b = c

output:-
0 1 1 2 3 5 8 13
