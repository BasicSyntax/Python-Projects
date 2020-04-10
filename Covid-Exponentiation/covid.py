

# start at 0 on January 10, iterate by += 1.1x every day
# find out how many weeks before 8 billion people are infected

x = 770000
y = 1.1
z = 1

while x <= (8 * (10 ** 9)):
    print(f'Covid patients are {x} on week {z} !')
    x = x*y
    z += 1

