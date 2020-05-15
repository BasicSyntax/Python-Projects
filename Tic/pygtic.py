import pygame
import random

pygame.init()

class Tiles(object):
    x = pygame.image.load('images/x_orange.png')
    o = pygame.image.load('images/o_blue.png')
    grid = pygame.image.load('images/bg_box.png')

    def __init__(self, colour, rect):
        self.colour = colour
        self.rect = rect
        win.blit(self.grid, self.rect)

    def draw_x(self):
        win.blit(self.x, self.rect)

    def draw_o(self):
        win.blit(self.o, self.rect)


def playMove():
    if 180 >= pygame.mouse.get_pos()[0]:
        if 180 >= pygame.mouse.get_pos()[1]:
            T1.draw_x()
            b[1] = 'X'
        elif 360 >= pygame.mouse.get_pos()[1] >= 180:
            T2.draw_x()
            b[2] = 'X'
        else:
            T3.draw_x()
            b[3] = 'X'
    elif 360 >= pygame.mouse.get_pos()[0] >= 180:
        if 180 >= pygame.mouse.get_pos()[1]:
            T4.draw_x()
            b[4] = 'X'
        elif 360 >= pygame.mouse.get_pos()[1] >= 180:
            T5.draw_x()
            b[5] = 'X'
        else:
            T6.draw_x()
            b[6] = 'X'
    else:
        if 180 >= pygame.mouse.get_pos()[1]:
            T7.draw_x()
            b[7] = 'X'
        elif 360 >= pygame.mouse.get_pos()[1] >= 180:
            T8.draw_x()
            b[8] = 'X'
        else:
            T9.draw_x()
            b[9] = 'X'


def compMove():
    possible_moves = [x for x, letter in enumerate(b) if letter == ' ' and x != 0]
    move = 0
    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = b[:]
            board_copy[i] = let
            if isWinner(board_copy, let):
                move = i
                if move == 1:
                    T1.draw_o()
                elif move == 3:
                    T3.draw_o()
                elif move == 7:
                    T7.draw_o()
                elif move == 9:
                    T9.draw_o()
                elif move == 2:
                    T2.draw_o()
                elif move == 4:
                    T4.draw_o()
                elif move == 6:
                    T6.draw_o()
                else:
                    T8.draw_o()
                return move

    if 5 in possible_moves:
        move = 5
        T5.draw_o()
        return move

    corners_open = []

    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners_open.append(i)

    if len(corners_open) >= 1:
        move = corners_open[random.randrange(0, (len(corners_open)))]
        if move == 1:
            T1.draw_o()
        elif move == 3:
            T3.draw_o()
        elif move == 7:
            T7.draw_o()
        else:
            T9.draw_o()
        return move

    edges_open = []

    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            edges_open.append(i)

    if len(edges_open) >= 1:
        move = corners_open[random.randrange(0, (len(corners_open)))]

    if move == 2:
        T2.draw_o()
    elif move == 4:
        T4.draw_o()
    elif move == 6:
        T6.draw_o()
    else:
        T8.draw_o()
    return move


def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[3] == le and bo[6] == le and bo[9] == le) or
            (bo[1] == le and bo[5] == le and bo[9] == le) or
            (bo[3] == le and bo[5] == le and bo[7] == le))


def redrawGameWindow():
    pygame.display.update()
    pass


screenWidth = 540
screenHeight = 540
font = pygame.font.SysFont('comicsans', 30, True)
b = [' ' for x in range(10)]
run = True

pygame.display.set_caption("TicTacToe with Machine Learning by BSpinks")

win = pygame.display.set_mode((screenWidth, screenHeight))
win.fill([255, 255, 255])
T1 = Tiles((0, 0, 0), (0, 0, 180, 180))
T2 = Tiles((0, 0, 0), (0, 180, 180, 180))
T3 = Tiles((0, 0, 0), (0, 360, 180, 180))
T4 = Tiles((0, 0, 0), (180, 0, 180, 180))
T5 = Tiles((0, 0, 0), (180, 180, 180, 180))
T6 = Tiles((0, 0, 0), (180, 360, 180, 180))
T7 = Tiles((0, 0, 0), (360, 0, 180, 180))
T8 = Tiles((0, 0, 0), (360, 180, 180, 180))
T9 = Tiles((0, 0, 0), (360, 360, 180, 180))

turn = 1
clickLoop = 0
# MAIN LOOP

print('Welcome to  Tic Tac Toe!')

while run:
    if clickLoop > 0:
        clickLoop += 1
    if clickLoop > 8:
        clickLoop = 0

    if pygame.mouse.get_pressed()[0] and clickLoop == 0:
        playMove()
        if b.count(' ') > 1:
            m = compMove()
            b[m] = 'O'
            if isWinner(b, 'O'):
                print('Sorry, O\'s won this time! .....1111111')
            elif isWinner(b, 'X'):
                print('X\'s won this time! Good Job! ....3333333')
        else:
            print('Tie Game! ....88888')
        clickLoop = 1

    redrawGameWindow()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
