playerOne = input('What is the name of player one? ')
playerTwo = input('What is the name of player two? ')
print('Welcome to The 100 Game %s and %s'%(playerOne,playerTwo))
print('You will each take turns to choose a number between 1 and 10.')
print('The first person to reach 100 is the winner')
print('%s, you will go first. %s, you will go second.'%(playerOne,playerTwo))
total = 0
playerOneTurn = True
while total < 100:
    if playerOneTurn == True:
        print('%s - pick a number from one to ten'%(playerOne))
    else:
        print('%s - pick a number from one to ten'%(playerTwo))
    choice = input()
    number = int(choice)
    total = total + number
    print('Thank you')
    print('The total is %i'%total)
    playerOneTurn = not playerOneTurn
if playerOneTurn = True:
    print('$s WINS'%(playerOne))
else:
    print('$s WINS'%(playerTwo))
