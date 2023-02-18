
age = 20
name = input('What is your name? ')
print('Hello ' + name)


age1 = 22
age2 = 34
age3 = 54

# Unpacking
ages = [22, 45, 55]
x, y, z = ages
print(ages[0])
print(x, y, z)


questions = ['Should you you subscribe', 'is coding cool?', ' is 1 + 1 = 3']
answers = ['yes', 'yes', 'no']


# Definiting a function

# Encapsulate code to make program less complicated


def quizgame():
    score = 0
    # Control flow ( for loop )
    for i in range(len(questions)):
        print(questions[i])
        ans = input('Please answer \n')
        if ans == answers[i]:
            print('correct')
            score += 1
        else:
            print('incorrect you fool')
 # How to print with both in
        print(f'final score: {score}')


# Running a function
quizgame()
