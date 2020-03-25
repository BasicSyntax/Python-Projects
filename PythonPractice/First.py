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
import matrix as matrix #  automatically added this import after i made matrix

print('Beaumont Spinks')  # Basic print function
print('*' * 10)  # This is known as an expression, its similar to a math equation
price = 10  # A variable, set to an Integer
print(price)  # Printing a variable does not use quotations
price = 20  # Setting a variable again can Override it with a different value
print(price)
name = ('Beau')  # all text must be in quotations
rating = 4.9  # A Float variable
is_published = True  # a Boolean variable, set to true or false.
# Good practice to set use underscores in a variable name to separate words
# Case sensitive for Booleans, always lowercase "false" and "true"
name = input('What is your name')  # Input function will request input from user and set it to a variable
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
print(type(age))  # type function prints the variable time
print(type(birth_year))
course = "Python's course for Beginners"  # Python uses ' or " quotation for strings, which messes up when used inside a string
print(course)
course = 'Python course for "Beginners"'  # using the opposite quotation mark will allow the inside marks to be printed
print(course)
course = ''' 
Hi Bob,

This is email format. 

This will all be printed line by line.

Kind Regards,

Spinks
'''  # have to put a commit after the final ''' because all lines in between are treated as a single paragraph of code
print(course)
course = 'Python course for Beginners'
print(course[0])  # Square brackets is used to print specific characters in a string, which start at 0
# e.g. a string of 1234 will be places 0123
print(course[-1])  # negative numbers in python in this sense will to to the end of the line and then backwards
# e.g. a string of 123456 will be places 0-5-4-3-2-1
print(course[0:3])  # using : you can choose a string of characters from one index to another
print(course[2:5])
print(course[:])  # if index are left blank it will print all characters from start to finish
print(course[1:-1])
first = 'John'
last = 'Smith'
print(first + ' [' + last + '] ' + ' is a coder')  # default way to print with variables
print(f'{first} [{last}] is a coder')  # formatted string to print with variables
print(len(course))  # len is short for length
print(course.upper())  # object oriented functions build into python
print(course.lower())  # also known as dot operators, or methods
print(course.title())  # first letter of each word is capitalized
print(course.find('P'))  # method to find a character
print(course.find('0'))  # if no character is found will return -1
print(course.find('Beginners'))
print(course.replace('Beginners', 'Absolute Beginners'))  # method to find and replace sequence of characters
print(course.replace('P', 'J'))
print('Python' in course)  # in operator checks if characters are in a string, returns boolean
print(10 + 3 - 6 * 2 / 4)  # arithmetic operators
print(5 / 3)  # division, returns a float
print(5 // 3)  # division, returns an integer, always rounds down
print(5 % 3)  # returns the remainder of a division
print(5 ** 3)  # exponentiation or power operator, e.g. 5 to the power of 3
x = 10
x = x + 3  # incrementing operator
x += 3  # enhances augmenter operator
x -= 5
print(10 + (3 - 6) / 7 * 11 ** 4)  # BIDMAS is law in python
x = 2.9
print(round(x))
print(abs(x))  # math methods, more with the math module

'''
if it's hot
    It's a hot day
    Drink plenty of water   
otherwise if it's cold
    It's a cold day
    Wear warm clothes
otherwise
    It's a lovely day
'''  # when programming large sections of code it can help to preplan the layout

is_hot = False

if is_hot:  # if statements to check and run code under conditions set, boolean check if 'True'
    print("It's a hot day")
print('Enjoy your day!')  # Python is incredible indent reliant, this line of code is not included in the 'if' function

is_cold = False

if is_hot:  # colon to open if statements along with else and elif statements
    print("It's a hot day")
    print('Drink plenty of water')
elif is_cold:  # elif is used after if where there are multiple conditions to be checked
    print("It's a cold day")
    print('Wear warm clothes')
else:
    print("It's a lovely day")
print('Enjoy your day!')
has_high_income = False
has_good_credit = True

if has_good_credit and has_high_income:  # Logical operators combine different conditions
    print('Eligible for loan')

if has_good_credit or has_high_income:  # the logic operators are, and, or, not
    print('Eligible for loan')

has_criminal_record = False

if not has_criminal_record:
    print('Eligible for loan')

# Personal note.
# This threw me off completely, python has 3 logical operators, and, or, not
# While Java has 6 :- ! not, & and, | or, ^ xor, && conditional and, || conditional or.

temperature = 30

if temperature > 30:  # conditional operators to check arithmetic situations
    print("It's a hot day!")
elif temperature == 30:
    print("The temperature is 30 degrees")
else:
    print("It's not a hot day!")

name = 'John'

if len(name) < 3:
    print('Name must be minimum of 3 characters!')
elif len(name) > 50:
    print('Name must be a maximum of 50 characters!')
else:
    print('Name looks good!')

i = 1
while i <= 5:  # while function runs a loop of the code until the condition is fulfilled
    print(i)
    i = i + 1
print("Done")

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break  # break is unique, terminates the if and while functions
else:  # else loop is not limited to if statements, need to be careful with indentation!
    print('Sorry you failed!')
for item in 'Python':  # for loops iterates items through a variable e.g. characters in a string
    print(item)
for item in ['Beau', 'Mont', 'Idris', 'Spinks']:  # an array of strings
    print(item)
for item in range(10):  # range is a python function which holds numbers in a series
    print(item)
for item in range(5, 10):  # using a comma you can set the start and the end
    print(item)
for item in range(5, 10, 2):  # a third number changes how many steps the range counts in (default is 1)
    print(item)
total = 0
prices = [10, 20, 30]
for item in prices:
    total += item
print(f"total cost = {total}")
for x in range(4):  # a nested loop is a technique to nest a loop within a loop to loop multiple loops iteratively
    for y in range(3):
        print(f'({x}, {y})')
numbers = [5, 2, 5, 2, 2]  # an array of numbers
x = 'x'
for item in numbers:
    x = ''
    while item > 0:
        x = x + 'x'
        item -= 1
    print(x)
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
numbers = [3, 6, 2, 151, 8, 4, 10]
max = numbers[0]
i = 0
for x in numbers:
    i += 1
    if x > max:
        max = x
        place = i
print(f'the largest number is {max} in the {place} position')
# matrix is a grid function to set values in rows and columns
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[2])  # row gets checked first
print(matrix[0][1])
matrix[0][1] = 45
print(matrix[0])
print(matrix[0][1])  # then column

for row in matrix:
    print(row)
    for item in row:
        print(item)
numbers = [5, 2, 7, 1, 4]
print(numbers)
numbers.append(24)
print(numbers)
numbers.insert(0, 14)
print(numbers)
numbers.pop()
print(numbers)
numbers.remove(2)
print(numbers)
numbers.clear()
print(numbers)
numbers = [5, 2, 7, 1, 1, 4]
print(numbers.index(5))
print(50 in numbers)
print(numbers.count(1))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
numbers2.append(10)
print(numbers)
print(numbers2)
# remove duplicates from a list challenge
challenge_tuple = (1, 8, 5, 2, 8, 5, 1) # a tuple similar to a list, but is immutable
unique = []

for x in challenge_tuple:
    if x not in unique:
        unique.append(x)
print(unique)
coordinates = (1, 2, 3)
x, y, z = coordinates # unpacking feature, fast and easy python method
print(y)
print(z)
#  Dictionary method or book, allocated information to set names
#  This can be used to store large amounts of data and call them with the name
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
customer["name"] = "Jack Smith"
print(customer["name"])
print(customer.get("birth_date"))
print((customer.get("birth_date", "Jan 1 1980")))
customer["birth_date"] = "Aug 23 1993"
print(customer.get("birth_date"))
phone = input("Phone: ")

p_number = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
word = ""
for ch in phone:
    word += p_number.get(ch, "!") + " "
print(word)