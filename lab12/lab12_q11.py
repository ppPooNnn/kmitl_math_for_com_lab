import random

event = ['head', 'tail']

percent = 0
sum_percent = 0
i = 0
while i < 3 :
    head = 0
    head_and_tail = 0
    for round in range(100000) :
        coin = random.choice(event)
        if coin == 'head' :
            head += 1
            if random.choice(event) == 'tail' :
                head_and_tail += 1
    percent = head_and_tail / head * 100
    sum_percent += percent
    i += 1
print(sum_percent / 3)