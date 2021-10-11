# James Shaw
# fortune.py
# 9/29/21

# Defining the final answers in a list.  Sets or Lists can be used in this function, but keep in mind that sets
# are not ordered, and may produce different results for the same inputs.
answers = [
    "You'll make a friend.",
    "It's your lucky day.",
    "You'll fall in love.",
    "Everybody likes you.",
    "You'll be rich.",
    "You'll be happy.",
    "You'll travel a lot.",
    "You'll be famous."
]

numbers1 = ["0", "1", "2", "3"]
numbers2 = ["4", "5", "6", "7"]

user_input = int(input("What's your favorite number?\n"))

# Using the .join() method to join an iterable container object's items into a single string, separated by the specified
# ", " characters.  ", ".join(numbers1) = "0, 1, 2, 3"
# If statement branching the program based on whether the user_input variable is divisible by 2.
if user_input % 2 == 0:
    second_user_input = int(input("Choose a number! " + ", ".join(numbers1) + "\n"))
else:
    second_user_input = int(input("Choose a number! " + ", ".join(numbers2) + "\n"))

print("Here's your fortune!\n")

# Print the output fortune answer from answers using the second_user_input variable as the index.
print(answers[second_user_input])
