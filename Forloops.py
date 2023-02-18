list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in list:
    # check for even
    if number % 2 == 0:
        print(number)
    else:
        print(f'odd numbers: {number}')


list_sum = 0

for num in list:
    list_sum = list_sum + num
    # if done inside loops and prints new sum every loop
print(list_sum)


myString = 'hello world'
for letter in myString:
    print(letter)


# TUPLE UNPACKING
tup = (1, 2, 3)
for item in tup:
    print(item)

myList = [(1, 2), (3, 4), (5, 6), (7, 8)]

for item in myList:
    print(item)

# TUPLE UNPACKING or

for a, b in myList:
    print(a)
    print(b)
# 1,2,3,4,5 etc..

d = {'k1': 1, 'k2': 2, 'k3': 3}
for key in d.items():
    print(key)
