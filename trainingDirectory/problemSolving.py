'''
numbers = [1,5,7,1,8,9]

newArr = []
for i in numbers:
    newArr.append(i)
print(newArr)
print(type(newArr))
numbers.insert(3,6)
del numbers[3]
del numbers[5]
print(numbers)
if 6 in numbers:
    print('hello bithes')
else:
    print('list not have a number 6')
'''

'''
numbers = [1,5,7,1,8,9]
newArr = len(numbers)
i=0
while i < newArr:
    print(numbers[i])
    i+=1
'''

numbers = [1,5,7,1,8,9,12]
for new in numbers:
    print(new)
newList = numbers[3:6:2]
print(newList)