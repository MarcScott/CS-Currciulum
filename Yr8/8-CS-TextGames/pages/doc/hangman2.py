import random
stage0=''
stage1 = '''
_______________'''
stage2 = '''
|
|
|
|
|
|
|\______________'''
stage3 = '''
__________
|/
|
|
|
|
|
|\______________'''
stage3 = '''
__________
|/       |
|        O
|
|
|
|
|\______________'''
stage4 = '''
__________
|/       |
|        O
|        |
|        |
|
|
|\______________'''
stage5 = '''
__________
|/       |
|        O
|       \|
|        |
|
|
|\______________'''
stage6 = '''
__________
|/       |
|        O
|       \|/
|        |
|
|
|\______________'''
stage7 = '''
__________
|/       |
|        O
|       \|/
|        |
|       /
|
|\______________'''
stage8 =r'''
__________
|/       |
|        O
|       \|/
|        |
|       / \
|
|\______________'''

stage = [stage0,stage1,stage2,stage3,stage4,stage5,stage6,stage7,stage8]
stageindex=0
correctGuesses = 0
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphalist = [letter for letter in alphabet]
words = ['cat','dog','fish']
word = random.choice(words)
gameOn = True
def displayWord():
    print('')
    display = ''
    for letter in word:
        if letter not in alphalist:
            display += letter + ' '
        else:
            display += '_ '
    print(display)

def displayStage():
    print(stage[stageindex])

def Guess():
    global stageindex
    global correctGuesses
    guess = input('Guess a letter ')
    if guess not in alphalist:
        print("Not valid, choose againr")
    elif guess not in word:
        stageindex+=1
        alphalist.remove(guess)
    else:
        alphalist.remove(guess)
        correctGuesses += 1

def checkEnd():
    global gameOn
    if correctGuesses == len(word):
        print('You Win')
        print(stage[stageindex])
        gameOn = False
    elif stageindex == 8:
        print('You Lose')
        print(stage[stageindex])
        gameOn = False

while gameOn == True:
    displayWord()
    displayStage()
    Guess()
    checkEnd()
