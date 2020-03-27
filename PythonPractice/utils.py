def find_max(numbers):
    mx = numbers[0]
    for number in numbers:
        if number > mx:
            mx = number
    return mx
