def corridor():
    print('You are in a long corridor')
    print('There are exits to the North and West')
    choice = ''
    choice = input('What would you like to do?')
    while choice not in ['North','West']:
        print('You can not do that')
        choice = input('What would you like to do?')
    if choice == 'North':
        room1()
    elif choice == 'West':
        room2()

def room2():
    print('You are in a small broom cupboard. The air smells musty and it is very dark')
    print('There are exits to the South')
    while choice not in ['South']:
        print('You can not do that')
        choice = input('What would you like to do?')
    if choice == 'South':
        corridor()

def room2():
    print('You are in a very dark room. You can not see anything. You know there is an exit to the West though')
    print('There are exits to the South')
    while choice not in ['West']:
        print('You can not do that')
        choice = input('What would you like to do?')
    if choice == 'West':
        corridor()
