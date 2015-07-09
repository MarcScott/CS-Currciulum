map = {'corridor':['room1','','','room2'],'room1':['','','corridor',''],'room2':['','corridor','','']}

commands = {'room1':room1,'room2':room2,'corridor':corridor}

roomItems = {'corridor':[],'room1':['torch'],'room2':['knife','pen']}

def Moving(location):
    rooms = map[location]
    directions = ['North','East','South','West']
    availableDirections = [directions[i] for i,j in enumerate(rooms) if rooms[i] != '']
    direction = input('Which direction would you like to go? ')
    while direction not in availableDirections:
        print('You can not go that way')
        direction = input('Which direction would you like to go? ')
    return rooms[directions.index(direction)]

def showItems(location):
    items = roomItems[location]
    if len(items) == 0:
        print('The room has no items you can get')
    elif len(items) == 1:
        print('There is a %s here'%(items[0]))
    elif len(items) == 2:
        print('There is a %s and a %s here'%(items[0],items[1]))
    else:
        print('You see a ',end=' ')
        for i, item in enumerate(items):
            if i == len(items) -1:
                print('and a '+item)
            else:
                print(item + ',',end=' ')


def corridor():
    print('You are in a long corridor')
    print('There are exits to the North and West')
    showItems('corridor')
    commands[Moving('corridor')]()


def room1():
    print('You are in a small broom cupboard. The air smells musty and it is very dark')
    print('There are exits to the South')
    showItems('room1')
    commands[Moving('room1')]()

def room2():
    print('You are in a very dark room. You can not see anything. You know there is an exit to the East though')
    showItems('room2')
    commands[Moving('room2')]()
