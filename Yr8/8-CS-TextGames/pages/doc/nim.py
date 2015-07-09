import random
print('Choose a number to move and a heap to move it from, seperated by a space')
print('')
print('|Heap 1|Heap 2|Heap 3|Move')

move = 'No move yet           '
heaps = [random.randrange(1,10),random.randrange(1,10),random.randrange(1,10)]
playerOne = True

while sum(heaps)> 0:
    try:
        number,heap = input('|  %i   |  %i   |  %i   |%s'%(heaps[0],heaps[1],heaps[2],move)).split()
        heap = int(heap)-1
        number = int(number)
        if heap < 0 or heap > 2:
            move = 'No move yet           '
        else:
            if heaps[heap]-number < 0:
                move = 'No move yet           '
            else:
                if playerOne == True:
                    player = 'Player One'
                else:
                    player = 'Player Two'
                heaps[heap]-=number
                move = (player +' takes '+ str(number) + ' from heap ' + str(heap+1)+'   ')
                playerOne = not playerOne
    except:
        move = 'No move yet                '
print(move +' and ' + player + '  wins')
