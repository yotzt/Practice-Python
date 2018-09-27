# Orginally created 09.11.2018. For Python3.
# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

# Beginning of script

# Starts by finding the user's name.
name = input("Give me your name: ")

print("Your name is " + name)

# Now the program gets the user's age and identifies it as a interger so the
# program can do math with it.
age = input("Enter your age: ")
age = int(age)
print(name + "'s age is " + str(age))

# Determine and display the number of years until the user turns 100 years old.
years_until_100 = 100 - age
print(name + " will be 100 years old in " + str(years_until_100) + " years.")

# Determine and display what year it will be when the user turns 100 years old.
year_when_100 = 2018 + years_until_100
print(name + " will be 100 years old in " + str(year_when_100) + ".")

# End of script
