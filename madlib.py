# madlib.py
# James Shaw
# 9/10/21

# Use newline character in order to give more space between output and input lines.
print("Welcome to my Madlib! For this game, I will ask you for some inputs then give you an output based on what you give me!\n")

# Gather input words as variables for use in the madlib string.  No inputs require any changes to other types of
# Python objects, as they are not being changed or used in any way that a normal string cannot handle.

flower_1 = input("Input a flower in plural format: ")

# Use inbuilt function within String objects to convert the string into an capitalized word.
# Most Python objects have inbuilt functions that come with the type of object you are using.  These inbuilt functions
# are known as Methods.
flower_1 = flower_1.capitalize()

flower_2 = input("Input a second flower in plural format: ")
# Use inbuilt function within String objects to convert the string into an capitalized word.
flower_2 = flower_2.capitalize()
color_1 = input("Input a color: ")
character = input("Input a single character: ")
integer = input("Input a whole, positive number: ")

# Here is an example of what is called an "f-string."  It is a formatted string using variables within
# "{/}" characters in order to fashion a string in a way that is more readable, but less functional than the standard
# inbuilt String format() function.  Use of this particular type of string is not best for all cases, but for this
# one, I deemed it the best choice.  Other ways to format string include the inbuilt .format() function, and some others
# that are less readable, in my personal opinion.
# This example also makes use of the Multi-line string that I introduced with the last assignment.

madlib = f"""{flower_1} are {color_1},
{flower_2} are blue.
There seems to be an unexpected '{character}',
in line {integer}."""

print(madlib)
