playerOne = input('What is the name of Player One? ')
playerTwo = input('What is the name of Player Two? ')
print('Welcome to The 100 Game %s and %s'%(playerOne,playerTwo))
print('You will each take turns to choose a number between 1 and 10.')
print('The first person to reach 100 is the winner')
total = 0
while total < 100:
    total += int( input('Give me a number between 1 and 10'))
