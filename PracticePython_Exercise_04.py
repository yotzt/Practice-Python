# Originally created on 09.20.2018. For Python3.
# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

# Beginning of the script

# The goal is to create a program that asks the user for a number and then
# prints out a lost of all the divisors of that numberself.

num = int (input ("Enter a number:"))

list_range = list(range(1,num+1))

divisor_list = []

for number in list_range:
    if num % number == 0:
        divisor_list.append(number)

print(divisor_list)

# End of the script
