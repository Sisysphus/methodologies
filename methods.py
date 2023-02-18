myList = [12, 4, 4, 5, 6, 321, 312]

myList2 = []


def calculate(func):
    '''So its going to take in  myList and returning the values
    by passing them into the second list'''
    for item in func:
        print(item)
        myList2.append(item)


calculate(myList)
print(myList2)
