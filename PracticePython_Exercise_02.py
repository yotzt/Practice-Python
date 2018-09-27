# Orginally created 09.11.2018. For Python3.
# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

# Beginning of the script

# To start, we need to ask the user for a number.

number = input("Please enter a number:")
number = int(number)

# We need to determine if the number is odd or even.
# For that, we can use the modulus operation (%) to see if there is a remainder.

remainder = number % 2
remainder = int(remainder)

# If there is a remainder, then we know the number is odd; if there is not a
# remainder, then we know the number is even. Use a conditional (if, elif, else)
# to displace the result in print.

if remainder == 0:
    print ("The number " + str(number) + " is even.")
else:
    print ("The number " + str(number) + " is odd.")

# End of the script.
