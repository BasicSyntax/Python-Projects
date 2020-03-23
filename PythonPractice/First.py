# -----------------------------------------------------------
# Hi there, my name is Beaumont Spinks and this is my practice file for Python
# Big thanks to "Programming with Mosh" on youtube
#
# The purpose of this file is to be used as a reminder for myself for Python
# To help me differentiate the subtle language differences between programming languages
#
# (C) 2020 Beaumont Spinks, London, England
# email beauspinks@gmail.com
# -----------------------------------------------------------


print('Beaumont Spinks') # Basic print function
print('*' * 10) # This is known as an expression, its similar to a math equation
price = 10 # A variable, set to an Integer
print(price) # Printing a variable does not use quotations
price = 20 # Setting a variable again can Override it with a different value
print(price)
name = ('Beau') # all text must be in quotations
rating = 4.9 # A Float variable
is_published = True # a Boolean variable, set to true or false.
# Good practice to set use underscores in a variable name to separate words
# Case sensitive for Booleans, always lowercase "false" and "true"
name = input('What is your name') # Input function will request input from user and set it to a variable
print('Hello, ' + name + '!')
birth_year = input('Birth year: ')
# age = 2020 - birth_year
# The above comment would have run an error
# Variables in python are automatically set to 'str'
age = 2020 - int(birth_year)
# birth_year is cast to an int from a str
int()
float()
bool()
# Above funtions to cast variables to another type
print(age)
print(type(age)) # type function prints the variable time
print(type(birth_year))
course = "Python's course for Beginners" # Python uses ' or " quotation for strings, which messes up when used inside a string
print(course)
course = 'Python course for "Beginners"' # using the opposite quotation mark will allow the inside marks to be printed
print(course)
course = ''' 
Hi Bob,

This is email format. 

This will all be printed line by line.

Kind Regards,

Spinks
''' # have to put a commit after the final ''' because all lines in between are treated as a single paragraph of code
print(course)
course = 'Python course for Beginners'
print(course[0]) # Square brackets is used to print specific characters in a string, which start at 0
# e.g. a string of 1234 will be places 0123
print(course[-1]) # negative numbers in python in this sense will to to the end of the line and then backwards
# e.g. a string of 123456 will be places 0-5-4-3-2-1
print(course[0:3]) # using : you can choose a string of characters from one index to another
print(course[2:5])
print(course[:]) # if index are left blank it will print all characters from start to finish
print(course[1:-1])
first = 'John'
last = 'Smith'
print(first + ' [' + last + '] ' + ' is a coder') # default way to print with variables
print(f'{first} [{last}] is a coder') # formatted string to print with variables
print(len(course)) # len is short for length
print(course.upper()) # object oriented functions build into python
print(course.lower()) # also known as dot operators, or methods
print(course.title()) # first letter of each word is capitalized
print(course.find('P')) # method to find a character
print(course.find('0')) # if no character is found will return -1
print(course.find('Beginners'))
print(course.replace('Beginners', 'Absolute Beginners')) # method to find and replace sequence of characters
print(course.replace('P', 'J'))
print('Python' in course) # in operator checks if characters are in a string, returns boolean
print(10 + 3 - 6 * 2 / 4) # arithmetic operators
print(5 / 3) # division, returns a float
print(5 // 3) # division, returns an integer, always rounds down
print(5 % 3) # returns the remainder of a division
print(5 ** 3) # exponentiation or power operator, e.g. 5 to the power of 3
x = 10
x = x + 3 # incrementing operator
x += 3 # enhances augmenter operator
x -= 5
print(10 + (3 - 6) / 7 * 11 ** 4) # BIDMAS is law in python
x = 2.9
print(round(x))
print(abs(x)) # math methods, more with the math module


'''
if it's hot
    It's a hot day
    Drink plenty of water   
otherwise if it's cold
    It's a cold day
    Wear warm clothes
otherwise
    It's a lovely day
''' # when programming large sections of code it can help to preplan the layout

is_hot = False

if is_hot: # if statements to check and run code under conditions set, boolean check if 'True'
    print("It's a hot day")
print('Enjoy your day!') # Python is incredible indent reliant, this line of code is not included in the 'if' function

is_cold = False

if is_hot: # colon to open if statements along with else and elif statements
    print("It's a hot day")
    print('Drink plenty of water')
elif is_cold: # elif is used after if where there are multiple conditions to be checked
    print("It's a cold day")
    print('Wear warm clothes')
else:
    print("It's a lovely day")
print('Enjoy your day!')