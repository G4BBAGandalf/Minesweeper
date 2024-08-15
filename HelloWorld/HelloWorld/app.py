from utils import find_max
import random
from pathlib import Path


class Dice:
    def __init__(self):
        self.x=1
        self.y=1

    def roll(self):
        self.x=random.randint(1,6)
        self.y=random.randint(1,6)
        return self.x,self.y


# members=['john', 'Mary', 'Peter','Bob']
# print(random.choice(members))

dice1 = Dice()
print(dice1.roll())

numbers = [0,4,2,7,9,1,4]
numberz =[1,3,2]
maximum = find_max(numberz)
print(maximum)

path = Path()
for file in path.glob('*'):
    print(file)