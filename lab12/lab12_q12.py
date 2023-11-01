import random

thai_goal_chance = 0.02
brazil_goal_chance = 0.10

event = {
            'thai_score' : 0,
            'thai_lose_but_score' : 0,
            'brazil_win' : 0,
            'thai_win' : 0
        }

for round in range(100000) :
    brazil_goal = 0
    thai_goal = 0
    for min in range(90) :
        if random.random() < thai_goal_chance :
            thai_goal += 1
        if random.random() < brazil_goal_chance :
            brazil_goal += 1
    if thai_goal >= 1 :
        event['thai_score'] += 1
    if thai_goal >= 1 and brazil_goal > thai_goal :
        event['thai_lose_but_score'] += 1
        event['brazil_win'] += 1
    elif brazil_goal > thai_goal :
        event['brazil_win'] += 1
    elif thai_goal > brazil_goal :
        event['thai_win'] += 1
print(sorted(event.items(), key=lambda x:x[1], reverse = True))