# Originally created on 09.11.2018. For Python3.
# https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

# Beginning of the script

# The goal is to write a program that displays all of the elements of the below
# list that are less than 5. Bonus: make the new list that has all the elements
# in one rather than one by one; write this in one line; ask the user for a
# number and return only elements smaller than the given number.

# This is the list we are given at the start.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Here we ask the user for a number to compare against the list and identify it
# as an interger.

num = int(input("Choose a number: "))

# Here we create a new list. This list will ultimately be the list of elements
# the fit the parameter of the user's given number.

new_list = []

# This is the part that adds the elements that fit the parameter into a new list.

for i in a:
    if i < num:
        new_list.append(i)

# Here we print the new list.

print (new_list)

# End of the script.
