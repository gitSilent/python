import random
ran_mas = []
while (len(ran_mas))<20:
    local_ran = random.randint(0,20)
    if local_ran not in ran_mas:
        ran_mas.append(local_ran)
print(ran_mas)