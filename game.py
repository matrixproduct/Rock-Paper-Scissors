import random

def play(shapes, user_shape, comp_shape, scr):
    if user_shape == comp_shape:
        scr += 50
        print(f'There is a draw ({user_shape})')
    else:
        l = len(shapes)
        comp_ind = shapes.index(comp_shape)
        user_win = [shapes[(comp_ind + i) % l] for i in range(1, (l-1) // 2 + 1)]
        if user_shape in user_win:
            scr += 100
            print(f'Well done. The computer chose {comp_shape} and failed')
        else:
            print('Sorry, but the computer chose', comp_shape)
    return scr


standard_shapes = ['rock', 'paper', 'scissors']
score = 0
random.seed()

user_name = input('Enter your name: ')
print('Hello,', user_name)

with open('rating.txt', 'r', encoding='utf-8') as f:
    for line in f:
        name, rating = line.strip().split()
        if name == user_name:
            score = int(rating)
s = input()
choices = standard_shapes if s == '' else s.split(',')
print('Okay, let\'s start')

while True:
    user_shape = input()
    if user_shape == '!exit':
        print('Bye!')
        break
    if user_shape == '!rating':
        print('Your rating:', score)
        continue
    if user_shape not in choices:
        print('Invalid input')
        continue
    comp_shape = random.choice(choices)
    score = play(choices, user_shape, comp_shape, score)


