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

def static_greeting():
    print('Hello Gabriel')

static_greeting()

def dynamic_greeting(name):
    print('Hello', name)

dynamic_greeting('Daniel')
dynamic_greeting('Naty')
dynamic_greeting('Chicago')

def find_treasure(array_of_string):
    for array in array_of_string:
        if(array == 'treasure'):
            print('Found the treasure')
            return True            

    print('Not here')
    return False        

find_treasure(['gold', 'garbage', 'treasure'])
find_treasure(['gold', 'garbage', 'trap'])