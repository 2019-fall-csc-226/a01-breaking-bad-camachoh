######################################################################
# Author: Dr. Scott Heggen      TODO: Change this to your name
# Username: heggens             TODO: Change this to your username
#
# Assignment: A01
#
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between 1988 and 1999. Also prints your friend's animal,
# and your compatibility with that friend's animal.
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
######################################################################

# Remember to read the detailed notes about each task in the A01 document.

######################################################################
# (Required) Task 1
# TODO Ask user for their birth year


# TODO Check the year using if conditionals, and print the correct animal for that year.
# See the a01_pets.py for examples


######################################################################
# (Required) Task 2
# TODO Ask the user for their friend's birth year


# TODO Similar to above, check your friend's year using if conditionals, and print the correct animal for that year


######################################################################
# (Optional) Task 3
# TODO Check for compatibility between your birth year and your friend's birth year
# NOTE: You can always assume the first input is your birth year (i.e., 1982 for me).
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.


# TODO print if you are a strong match, no match, or in between
my_input = input('What year were you born in?')

if my_input == '2000':
    print("You're a hot breath dragon. Eww ")
elif my_input == '2001':
    print("You're a Slithering Snake")
elif my_input == '2002':
    print("You're a slow horse")
elif my_input == '2003':
    print("You're the Greatest Of All Time (Goat)")
elif my_input == '2004':
    print("You're a crazy monkey")
elif my_input == '2005':
    print("You're a loud rooster")
elif my_input == '2006':
    print("You're a dawg woof!")
elif my_input == '2007':
    print("You're a stinky pig. Eww")
elif my_input =='2008':
    print("You're a roaring dragon")
elif my_input == '2009':
    print("You're a sneaky snake")
elif my_input == '2010':
    print("You're an ugly horse")
elif my_input =='2011':
    print("You're a goat with a goatee")



friend_input = input('What year was your friend born?')

if friend_input == '2001':
    print("You're a snake")
elif friend_input == '2002':
    print("You're a horse")
elif friend_input == '2003':
    print("You're a goat")
elif friend_input == '2004':
    print("You're a monkey")
elif friend_input == '2005':
    print("You're a rooster")
elif friend_input == '2006':
    print("You're a dog")
elif friend_input == '2007':
    print("You're a pig")
elif friend_input == '2008':
    print("You're a dragon")
elif friend_input == '2009':
    print("You're a snake")
elif friend_input == '2010':
    print("You're a horse")
elif friend_input == '2011':
    print("You're a goat")
elif friend_input == '2012':
    print("You're a dragon")

