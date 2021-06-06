import random

# result= random.randint(50, 60)
# result_percent= random.uniform(0, 100)

# if result_percent < 22.5:
#     result *= 2

# print(result)
# print(result_percent)

  

lists = [0, 50, 100, 1000]
result= random.choice(lists)
print(result)

random.shuffle(lists)
print(lists)    