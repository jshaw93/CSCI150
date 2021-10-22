# James Shaw
# slotmachine.py
# 10/11/21

import random

stop_bool = False

while not stop_bool:
    slot_numbers_list = []
    print("Python Slot Machine")
    # For loop using the _ character as the iterated value name.  We use the _ here as it signifies that we are not using
    # the value, only the loop itself; otherwise, I would give the value a proper variable name.
    # I use this loop to populate the list with our random variables.
    for _ in range(3):
        number = random.randint(0, 9)
        number = str(number)
        slot_numbers_list.append(number)

    # Use the string.join() method to join the numbers list objects into a single string, separated by a space.
    print(" ".join(slot_numbers_list))

    # Gather counts for the 0th and 1st index of slot_numbers_list, we do not need more than two of the three indexes.
    count_0 = slot_numbers_list.count(slot_numbers_list[0])
    count_1 = slot_numbers_list.count(slot_numbers_list[1])

    if count_0 == 3:
        print("Jackpot!!")
    elif count_0 == 2 or count_1 == 2:
        print("Matched 2!!")
    else:
        print("Sorry you lost!")

    user_input = input("Play again? (y): ").lower()
    if user_input != 'y':
        stop_bool = True
    print("\n")
print("Thank you for playing!")
