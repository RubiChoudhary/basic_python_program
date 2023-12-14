#Call by Value: - when the value is passed as immutable
def vaule(a):
    print(a)
b = [1,2]
vaule(b)
c = [1,2]
vaule(c)

#Call by Reference: - when the value is passed as mutable
def refernece(a):
    a.append(1)
a = [1,2]
refernece(a)
print(a)
refernece(a)
print(a)