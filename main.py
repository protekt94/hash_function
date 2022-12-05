import random
import math

numbers = (random.randint(1, 1000) for num in range(30))
a = (math.sqrt(5) - 1) / 2
n = 10
hush = []
for coll, num in enumerate(numbers):
    hush_num = math.ceil(n * (num * a))
    hush.append(hush_num)
    if hush_num in hush[:coll]:
        print(f'h({num}) = {hush_num} - коллизия')
    else:
        print(f'h({num}) = {hush_num}')
