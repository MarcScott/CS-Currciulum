inventory = []
hitPoints = 100
roomItems = {'room1':['torch','gun','dog'],'room2':['knife']}

def corridor():
    print('You are in a long corridor. There is a door to the East and another to the North')
    action = input('What would you like to do? ')
    while action not in ('e','n'):
        print('You can not do that')
        action = input('Which way would you like to go? ')
    if action == 'n':
        room1()
    else:
        room2()

def room1():
    print('You find yourself in a small cupboard.')
    roomItem = roomItems['room1']
    if len(roomItem) == 0:
        print('The room is empty')
    elif len(roomItem) == 1:
        print('There is a %s here'%(roomItem[0]))
    elif len(roomItem) == 2:
        print('There is a %s and a %s here'%(room[0],room[1]))
    else:
        print('You see a ',end=' ')
        for i, item in enumerate(roomItem):
            if i == len(roomItem) -1:
                print('and a '+item)
            else:
                print(item + ',',end=' ')
    print('There is a door to the south')
    action = input('What would you like to do')
    while action not in roomItem and action not in ['s']:
        print('You can not do that')
        action = input('What would you like to do')
    while action not in ['s'] or action in roomItem:
        print('You take the %s'%action)
        inventory.append(action)
        roomItems['room1'].remove(action)
        action = input('What would you like to do')
    print('You go south')
    corridor()
