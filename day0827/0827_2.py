import random

total_num = 10000
count = 0
for i in range(1,21):
    if total_num <= 0:
        break
    if random.randint(1,10) < 5:
        continue
    else:
        total_num = total_num - 1000
    count += 1
print(count)