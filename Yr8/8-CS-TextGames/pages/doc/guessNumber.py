import random

number = random.randrange(1,100)
jimichoice = 0

while jimichoice != number:
    jimichoice = int(input('Choose a number'))
    if jimichoice == number:
        print('well done')
    elif jimichoice > number:
        print('bad luck, too big')
    elif jimichoice < number:
        print('bad luck too small')
