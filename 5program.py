d = {'a':1, 'b':2}
dd =['a','b','c']
sum1 = 0
for i in dd:
    if d.get(i) != None:
        sum1 = sum1 + d.get(i)
print(sum1)