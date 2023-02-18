def f(x):
    return x + 2


def ageCalculator(age):
    initialAge = input('How old are you ? ')
    initialAge = int(initialAge)
    return initialAge + 20


nextAge = ageCalculator(20)
print(nextAge)

