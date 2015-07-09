import random
choices = ['rock','paper','scissors','lizard','spock']
computerChoice = random.choice(choices)
playerChoice = input('rock, paper, scissors, lizard or spock? ')
print('I choose %s'%(computerChoice))

rules = {'spock':['scissors','rock'],'scissors':['lizard','paper'],'paper':['rock','spock'],'rock':['scissors','lizard'],'lizard':['spock','paper']}
if playerChoice == computerChoice:
    print('Draw')
elif computerChoice in rules[playerChoice]:
    print('You win')
else:
    print('I win')

