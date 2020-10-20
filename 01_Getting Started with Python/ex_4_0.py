##RANDOM MODULE
""""Program produces 10 random numbers between 0.0 and up to but not including 1.0"""
import random

for i in range(10):
    i = random.random()
    print(i)


""""Program produces 8 random integers between specified low and high values(including)"""
for i in range(8):
    i = random.randint(2,10)
    print(i)

"""Random choice"""
choices = [1, 2, 3]
print("Random choice: ", random.choice(choices))