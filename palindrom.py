string = input("enter the string: ")
reverse = ""
for i in range(len(string)-1,-1,-1):
    reverse= reverse + string[i]
print("this is reverse of string: ",reverse)
if string == reverse:
    print("palindrom")
else:
    print("not")