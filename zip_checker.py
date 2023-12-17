num = [1,2]
num1 = [3,4]
for list, list1 in zip(num,num1):
    print('first list number {0} second is {1}'.format(list,list1))

num = {"hello" : 1,"hi" :2}
num1 = {"nothing" : 3, "why" :4}

for list, list1 in zip(num,num1):
    print('first list number {0} second is {1}'.format(list,list1))