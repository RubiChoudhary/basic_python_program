a = input('enter string: ')
b = input('enter string: ')
d = {}
dd = {}
if len(a) != len(b):
    print("cannot be a anagram")
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
