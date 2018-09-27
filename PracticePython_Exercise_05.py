# Originally created on 09.25.2018. For Python3.
# https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

# Beginning of the script.

# The goal of this program is to compare two given lists and return a list of
# the common elements.

# These are the two list we are given at the start:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Here we create a new list, called "c".

c = []

# This part of the script compares a and b and adds (appends) the items that
# exist in both a and b to c. The third line prevents duplicates.

for item in a:
    if item in b:
        if item not in c:
            c.append(item)

# This prints the items in c, which is the solution.

print (c)

# End of the script.
