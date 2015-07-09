map = {'corridor':['room1','','','room2'],'room1':['','','corridor',''],'room2':['','corridor','','']}

commands = {'room1':room1,'room2':room2,'corridor':corridor}

def Moving(location):
    rooms = map[location]
    directions = ['North','East','South','West']
    availableDirections = [directions[i] for i,j in enumerate(rooms) if rooms[i] != '']
    direction = input('Which direction would you like to go? ')
    while direction not in availableDirections:
        print('You can not go that way')
        direction = input('Which direction would you like to go? ')
    return rooms[directions.index(direction)]
    
def corridor():
    print('You are in a long corridor')
    print('There are exits to the North and West')
    commands[Moving('corridor')]()

def room1():
    print('You are in a small broom cupboard. The air smells musty and it is very dark')
    print('There are exits to the South')
    commands[Moving('room1')]()

def room2():
    print('You are in a very dark room. You can not see anything. You know there is an exit to the East though')
    commands[Moving('room2')]()
