myList = [1, 2, 3, 4, 5, 6]

for item in enumerate(myList):
    print(item)


def myfunc(a, b):
    # returns 5% sum of and b
    return sum((a, b)) * 0.05


print(myfunc(1, 3))


def myfunc(*args):
    return sum(args) * 0.05


print(myfunc(40, 50))


def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I didnt find any fruit here')


myfunc(fruit='apple', veggie='carrots')


s = 'hello'

s = 'y'+s[:len(s)]

print(s)

print(len(s))
