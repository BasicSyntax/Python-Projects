import cmath
from os import system

# system("clear")

class PixelDensityCalculator(object):
    
    def __init__(self, horizontal, vertical, diagonal):
        self.horizontal = horizontal
        self.vertical = vertical
        self.diagonal = diagonal

    
    def ppi_calculator(self):
        diagonal_res = cmath.sqrt((self.horizontal ** 2 + self.vertical ** 2))
        return diagonal_res / self.diagonal
