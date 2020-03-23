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
'''
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
print(f'{first} [{last}] is a coder') # formatted string to print with varuables
print(len(course)) # len is short for length
course.upper() # object oriented functions build into python
course.lower() # also known as dot operators, or methods