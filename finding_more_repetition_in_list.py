a = [1,2,3,4,5,6,3,2,2]
anum = set()
for i in a:
    if i in anum:
        print(i)
        break
    else:
        anum.add(i)
else:
    print("no reptition")
