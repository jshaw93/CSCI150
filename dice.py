# James Shaw
# dice.py
# 10/18/21

import random

# Dictionaries are so useful!  Since the problem asks us to track the relationship between two variables, the
# summation of the two die and how many times that summation is rolled, a dictionary is the perfect way to store the
# information we need.
roll_dictionary = {
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0
}

# Producing the 100 rolls of the 6-sided die, and incrementing the dictionary with the results
for _ in range(100):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    summation = dice1 + dice2
    roll_dictionary.update({summation: roll_dictionary[summation] + 1})

for key in roll_dictionary:
    # Using a fun little trick in python that allows you to multiply a string, reproducing and concatenating
    # the string as many times as you multiply it.  "*" * 8 = "********"
    # Python is the only language I am aware of that allows this kind of functionality, without having to program a loop yourself.
    if key < 10:
        print(f" {key}s:", roll_dictionary[key] * "*")
    else:
        print(f"{key}s:", roll_dictionary[key] * "*")
