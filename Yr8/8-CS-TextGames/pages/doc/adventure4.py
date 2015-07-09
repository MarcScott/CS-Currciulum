map = {'corridor':['room1','','','room2'],'room1':['','','corridor',''],'room2':['','corridor','','']}

roomItems = {'corridor':[],'room1':['torch'],'room2':['knife','pen']}

playerItems = []

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

def action(location):
    print('What would you like to do')
    print('1. Take an item')
    print('2. Use an item')
    print('3. Leave')
    print('4. Interact')
    print('5. Look again')
    choice = input()
    if choice == '1':
        takeItems(location)
    elif choice == '2':
        useItem()
    elif choice == '3':
        commands[Moving(location)]()
    elif choice == '4':
        fight(location)
    elif choice == '5':
        command[location]()
    else:
        print('You can not do that')
        commands[location]()

def takeItems(location):
    items = roomItems[location]
    if len(items) == 0:
        print('There is nothing to take')
        action(location)
    item = input('What would you like to take? ')
    while item not in items:
        print('You can not see that here')
    playerItems.append(item)
    print('You take the %s'%(item))
    roomItems[location].remove(item)
    action(location)

def useItems(location):
    print('Not implemented yet')
    action(location)
    
def fight(location):
    print('Not implemented yet')
    action(location)
    
def corridor():
    print('You are in a long corridor')
    print('There are exits to the North and West')
    showItems('corridor')
    action('corridor')

def room1():
    print('You are in a small broom cupboard. The air smells musty and it is very dark')
    print('There are exits to the South')
    showItems('room1')
    action('room1')

def room2():
    print('You are in a very dark room. You can not see anything. You know there is an exit to the East though')
    showItems('room2')
    action('room2')

commands = {'room1':room1,'room2':room2,'corridor':corridor}
corridor()
