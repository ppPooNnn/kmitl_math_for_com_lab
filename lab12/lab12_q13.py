import random

event = ['A', 'B', 'C']
choose = 'A'
sum_win = 0
for round in range(100000) :
    reward = random.choice(event)
    if reward == choose :
        sum_win += 1
chance = sum_win / 100000 * 100
print('Chance if you not change the box', chance)
sum_win = 0

for round in range(100000) :
    reward = random.choice(event)
    choose = random.choice([reward,'wrong'])
    if reward == choose :
        sum_win += 1
chance = sum_win / 100000 * 100
print('Chance if you change the box', chance)