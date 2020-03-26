from ppi import PixelDensityCalculator
from sys import exit
from os import system
from time import sleep

def print_menu():
    while True:
        # system("clear")
        print "1.\tCalculate Pixel Density"
        print "2.\tExit"

        while True:
            try:
                choice = int(raw_input("\n> "))
            except ValueError:
                print "Enter 1 or 2"
                sleep(2)
                continue

            if choice == 1:
                take_details()
            elif choice == 2:
                # system("clear")
                exit(0)
            else:
                print "Enter 1 or 2"
                sleep(2)

def take_details():
    # system("clear")
    details = ["Horizontal Pixel Count",
               "Vertical Pixel Coint",
               "Diagonal Screen Size in Inches"]
    numbers = range(3)
    i = 0

    while i != len(details):
        try:
            numbers[i] = float(raw_input("%s : " % details[i]))
            i += 1
        except ValueError:
            print "Not a valid number, please try again!"
            i - 1
            continue

    x = PixelDensityCalculator(numbers[0], numbers[1], numbers[2])
    result = x.ppi_calculator()
    
    print "\nThe pixel density of the display is %.2f pixels/inch."\
            % result.real

    raw_input()
    
    print_menu()
