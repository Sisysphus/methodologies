thisDict = {
    "brand": "ford",
    "model": "mustang"
}


a, b = thisDict
for chr, item in thisDict.items():
    print(chr, item)


celcius = [1, 2, 3, 4, 9]

for temp in celcius:
    fahrenheit = (9/5)*temp + 32
    print(fahrenheit)


itemArray = {
    "Height": 42,
    "Weight": "200lbs",
    "Laptop": "Macbook"
}


a, c, b = itemArray
print(a, c, b)


for i in itemArray:
    print(i, itemArray[i])

for l, x in itemArray.items():
    print(l, x)


loopList = {
    'a': 'b',
    'c': 'd',
    'e': 'f',
    'g': 'h'
}

for key, pair in loopList.items():
    print(key, pair)

for i in loopList:
    print(i, loopList[i])
print(loopList.keys())
print(loopList.values())


for key, value in loopList.items():
    if key == 'a':
        print('hi')
        break
    else:
        print(key, value, "hi")


story1 = input('Do you want to go right or left"? ')

if story1 == 'right':
    input('/n You have chosen death! which way now? up or down')
elif story1 == "left":
    input('You have chosen correctly, left or right?')
    print('you may proceed')
