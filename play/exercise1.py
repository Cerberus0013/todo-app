# create a random number generatot that take in a lower and upper number then spits out a number in betwwe

import random


lower_number = int(input("Enter the lower bound: "))
upper_number = int(input("Enter the upper bound: "))

print(random.randint(lower_number, upper_number))