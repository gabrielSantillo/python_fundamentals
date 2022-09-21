x = -10
name = 'gabriel'
is_true = False
print(x)
print(name)
print(is_true)

if(x > 10):
    print('That is larger than 10')
else:
    print('That is not larger than 10')

if(x < 0 and is_true == True):
    print('Negative and True')
elif(x > 0 and is_true == False):
    print('Positive and False')
elif(x > 100 or is_true == True):
    print('Large or True')
else:
    print('I dont know')

names = ['Gabriel', 'Natalia', 'Chicago']
array_numbers = [26, 37, 1]

for name in names:
    print('Look at this name: ', name)

for num in array_numbers:
    print('Look at this number: ', num)