import random
import math

n = 0
usr_num = 0
print('Welcome to the Guessing Game')
print('How hard do you want the game to be?!')
d = input('Easy, Normal, Hard, Expert, Evil:')
if d == 'Easy':
    com_num = random.randint(1,10)
elif d == 'Normal':
    com_num = random.randint(1,100)
elif d == 'Hard':
    com_num = random.randint(1,1000)
elif d == 'Expert':
    com_num = random.randint(1,10000)
elif d == 'Evil':
    com_num = random.randint(1,1000000)

while 1 < 2:
    #print(com_num)
    n = n + 1
    usr_num = int(input("Enter Your Guess :"))
    if com_num == usr_num:
        print('You Win! Congrats')
        print('You have been able to guess the right Number in', n, 'Tries')
        break
    elif com_num > usr_num:
        print('Up, Up, Up, ⬆️')
    elif com_num < usr_num:
        print('Down, Down, Down, ⬇️')
    
