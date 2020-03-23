print('Beaumont Spinks') # Basic print function
print("*" * 10) # This is known as an expression, its similar to a math equation
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
print("Hello, " + name + "!")
birth_year = input('Birth year: ')
# age = 2020 - birth_year
# The above comment would have run an error
# Variables in python are automatically set to 'str'
age = 2020 - int(birth_year)
# birth_year is cast to an int from a str
int()
float()
bool()
# Above funtions to cast variables to other properties
print(age)

sad