from random import shuffle
from random import randint
x = 100

while x < 100:
    print('youre less than')
else:
    print('youre growings')


x = [1, 2, 3]
for item in x:
    # Comment
    pass
print('end of script')


list = ['adam', 'brian']

for x in enumerate(list):
    print(x[0])


# x = 100

# while x > 20:
    # if x == 21:
    # break
   # x -= 1
  #  print
#

alphabet = ['a', 'b', 'c', 'd']

for i, chr in enumerate(alphabet):
    print(i, chr)


a = 'x' in [1, 2, 3]
print(a)


g = 'mykey' in {'mykey': 345}
print(g)


myList = [10, 20, 30, 40, 50]
minimum = min(myList)
print(minimum)


shuffle(myList)
print(myList)


enumeratedList = ['a', 'd', 23, 32]

print(enumeratedList[-1:])


last_ele = enumeratedList.pop()
print(last_ele)
