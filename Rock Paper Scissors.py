import random
c = ['Rock', 'Paper', 'Scissors']


player = False
while player == False:
    cc = random.choice(c)
    p = input('Your Turn : Rock, Paper or Scissors?')
    if p == cc:
        print('Tie, Do you want to try Again?')
        t = input(('y/n'))
        if t == 'y':
            continue
        else:
            print('Have a nice Day')
            player = True
    if p == 'Rock' and cc == 'Paper':
        print('You Lost! Do you want to try again?')
        t = input(('y/n'))
        if t == 'y':
            continue
        else:
            print('Have a nice Day')
            player = True
    elif p == 'Rock' and cc == 'Scissors':
        print('You Win! Do you want to try again?')
        t = input(('y/n'))
        if t == 'y':
            continue
        else:
            print('Have a nice Day')
            player = True
    elif p == 'Paper' and cc == 'Scissors':
        print('You Lost! Do you want to try again?')
        t = input(('y/n'))
        if t == 'y':
            continue
        else:
            print('Have a nice Day')
            player = True
    elif p == 'Paper' and cc == 'Rock':
        print('You Win! Do you want to try again?')
        t = input(('y/n'))
        if t == 'y':
            continue
        else:
            print('Have a nice Day')
            player = True
    elif p == 'Scissors' and cc == 'Rock':
        print('You Lost! Do you want to try again?')
        t = input(('y/n'))
        if t == 'y':
            continue
        else:
            print('Have a nice Day')
            player = True
    elif p == 'Scissors' and cc == 'Paper':
        print('You Win! Do you want to try again?')
        t = input(('y/n'))
        if t == 'y':
            continue
        else:
            print('Have a nice Day')
            player = True        