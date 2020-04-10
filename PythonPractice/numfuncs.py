# https://programmingwithmosh.com/python/python-exercises-and-questions-for-beginners/
# Coding Exercise 1


def largest_of_two(a, b):
    if a > b:
        return a
    else:
        return b


# 2


def fizz_buzz(a):
    if a % 15 == 0:
        return "FizzBuzz !"
    elif a % 3 == 0:
        return "Fizz !"
    elif a % 5 == 0:
        return "Buzz !"
    else:
        return "No Fizz, No Buzz."


# 3


def drive_speed(speed):
    if speed < 70:
        return "OK !"
    elif speed < 75:
        return "Slow Down !"
    elif speed <= 80:
        return f"Points: {(speed - 70) // 5}"
    else:
        return "Licence Suspended !"


# 4


def showNumbers(limit):
    i = 0
    while i <= limit:
        if i % 2 == 0:
            print(f"{i} EVEN ")
        else:
            print(f"{i} ODD")
        i += 1


# 5


def sum_of_multiples(limit):
    x = 0
    i = 0
    while i <= limit:
        if i % 3 == 0 or i % 5 == 0:
            x += i
        i += 1
    return x


# 6


def show_stars(rows):
    i = 1
    while i <= rows:
        print("*" * i)
        i += 1


# cmd-dot will do the ... above

# 7


def prime_numbers(limit):
    it_num = 0

    # iterate from 0 > numb . Works
    while it_num <= limit:
        # print(f"*** it_num is {it_num}")

        # check for half of i , round down
        hnum = it_num // 2
        # print(f"*** hnum is {hnum}")
        it_hnum = 2

        # Bool for if prime = true
        prime = True

        # divide i by every number between 0 and half of i
        while it_hnum <= hnum:

            check_prime = it_num % it_hnum
            # print(it_num)
            # print(check_prime)
            # print(f"{it_num} / {it_hnum} = {it_num / it_hnum}")

            it_hnum += 1

            # change prime to False if any division has no remainder
            if check_prime == 0:
                prime = False

        # prime check
        if prime:
            print(f'{it_num} is prime!')

        it_num += 1

    return "Finished !"


print(prime_numbers(1551))
