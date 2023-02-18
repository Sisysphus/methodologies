

st = 'Print only the words that start with s in this sentence'


for word in st.split():
    if word[0] == 's':
        print(word)


for x in range(0, 10):
    if x % 2 == False:
        print(x)


alist = range(0, 50)

alist2 = []

for x in alist:
    if x % 2 == False:
        alist2.append(x)

print(alist2)


xt = 'Print every word in this sentence that has an even number of letters'
xt = xt.split()

for word in xt:
    if len(word) % 2 == False:
        print(word, 'This one is even')


printedValues = range(0, 100)


for x in printedValues:
    if x % 3 == False:
        print('Buzz')
    elif x % 5 == False:
        print('Fizz')
    elif x % 5 and x % 3 == False:
        print('FizzBuzz')


pt = 'Create a list of the first letters of every word in this string'
pt = pt.split()

lt = []
for i in pt:
    lt.append(i[0])
print(lt)
