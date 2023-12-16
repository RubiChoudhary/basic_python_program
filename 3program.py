# sum in dictionary
d = {'a':1, 'b':2}
dd =['a','b','c']
sum1 = 0
for i in dd:
    if d.get(i) != None:
        sum1 = sum1 + d.get(i)
print(sum1)




# count of letters
a = ['a' ,'a','s' ,'d' ,'f' ,'g' ,'h' ,'a' ,'s' ,'c' ,'u' ,'i' ,'h' ,'i']
# type1 count of letters
d = {}
for item in a:
    if d.get(item) is None:
        d[item] = 1
    else:
        d[item] = d[item] + 1
print(d)
dd={}

# type2 count of letters
for item in a:
    if item in dd:
        dd[item] += 1
    else:
        dd[item] = 1
print(dd)

# type3 count of letters
new_dict = {}
for item in a:
    new_dict[item] = new_dict.get(item, 0) + 1

print(new_dict)



a = 'bac'
b = 'abcd'
d = {}
dd = {}
for items in a:
    if d.get(items) is None:
        d[items] = 1
    else:
        d[items] = d[items] + 1

for item in b:
    if dd.get(item) is None:
        dd[item] = 1
    else:
        dd[item] += 1
flag = True
for key, val in d.items():
    if dd.get(key) != val:
        print("Not anagram")
        flag = False
        break
if flag is True:
    print("Anagram")
else:
    print("Not a anagram")
