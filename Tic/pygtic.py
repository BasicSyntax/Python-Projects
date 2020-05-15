import pygame

pygame.init()


class Tiles(object):
    x = pygame.image.load('images/x_orange.png')
    o = pygame.image.load('images/o_blue.png')
    grid = pygame.image.load('images/bg_box.png')

    def __init__(self, colour, rect):
        self.colour = colour
        self.rect = rect
        win.blit(self.grid, self.rect)
        # pygame.draw.rect(win, self.colour, self.rect, 4)  # 1

    def draw_x(self):
        win.blit(self.x, self.rect)

    def draw_o(self):
        win.blit(self.o, self.rect)


def playMove():
    if 180 >= pygame.mouse.get_pos()[0]:
        if 180 >= pygame.mouse.get_pos()[1]:
            T1.draw_x()
            insertLetter('X', 1)
        elif 360 >= pygame.mouse.get_pos()[1] >= 180:
            T2.draw_x()
            insertLetter('X', 2)
        else:
            T3.draw_x()
            insertLetter('X', 3)
    elif 360 >= pygame.mouse.get_pos()[0] >= 180:
        if 180 >= pygame.mouse.get_pos()[1]:
            T4.draw_x()
            insertLetter('X', 4)
        elif 360 >= pygame.mouse.get_pos()[1] >= 180:
            T5.draw_x()
            insertLetter('X', 5)
        else:
            T6.draw_x()
            insertLetter('X', 6)
    else:
        if 180 >= pygame.mouse.get_pos()[1]:
            T7.draw_x()
            insertLetter('X', 7)
        elif 360 >= pygame.mouse.get_pos()[1] >= 180:
            T8.draw_x()
            insertLetter('X', 8)
        else:
            T9.draw_x()
            insertLetter('X', 9)


# Computer playing side starts here .....


def compMove():
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if isWinner(board_copy, let):
                move = i
                if move == 1:
                    T1.draw_o()
                    print('winning jy543')
                elif move == 3:
                    T3.draw_o()
                    print('winning jy124')
                elif move == 7:
                    T7.draw_o()
                    print('winning as254')
                elif move == 9:
                    T9.draw_o()
                    print('winning ky876')
                elif move == 2:
                    T2.draw_o()
                    print('winning bf34')
                elif move == 4:
                    T4.draw_o()
                    print('winning sd234')
                elif move == 6:
                    T6.draw_o()
                    print('winning nb235')
                else:
                    T8.draw_o()
                    print('winning mjh4356')
                print('move = ' + str(move))
                return move

    if 5 in possible_moves:
        move = 5
        T5.draw_o()
        print('mid move')
        print('move = ' + str(move))
        return move

    corners_open = []

    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners_open.append(i)
            print(i)

    if len(corners_open) >= 1:
        move = selectRandom(corners_open)
        if move == 1:
            T1.draw_o()
            print('corn move 1')
        elif move == 3:
            T3.draw_o()
            print('corn move 3')
        elif move == 7:
            T7.draw_o()
            print('corn move 7')
        else:
            T9.draw_o()
            print('corn move 9')
        print('move = ' + str(move))
        return move

    edges_open = []

    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            edges_open.append(i)

    if len(edges_open) >= 1:
        move = selectRandom(corners_open)

    if move == 2:
        T2.draw_o()
        print('edge move 2')
    elif move == 4:
        T4.draw_o()
        print('edge move 4')
    elif move == 6:
        T6.draw_o()
        print('edge move 6')
    else:
        T8.draw_o()
        print('edge move 8')
    print('move = ' + str(move))
    return move


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[3] == le and bo[6] == le and bo[9] == le) or
            (bo[1] == le and bo[5] == le and bo[9] == le) or
            (bo[3] == le and bo[5] == le and bo[7] == le))


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def isBoardFull(b):
    if b.count(' ') > 1:
        return False
    else:
        return True


def redrawGameWindow():
    pygame.display.update()
    pass


def main():
    print(board)
    if not isBoardFull(board):
        if isWinner(board, 'O'):
            print('Sorry, O\'s won this time! .....a123')
        if not (isWinner(board, 'X')):
            mo = compMove()
            if mo == 0:
                print(board)
                print('Tie Game! .....l123')
            else:
                insertLetter('O', mo)
                print(board)
                return
            return
        else:
            print(board)
            print('X\'s won this time! Good Job! ....h456')
    else:
        print(board)
        print('Tie Game! ....j214')


# ends here .....


screenWidth = 540
screenHeight = 540
font = pygame.font.SysFont('comicsans', 30, True)
board = [' ' for x in range(10)]
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
        # main()
        if not isBoardFull(board):
            m = compMove()
            print('compmove')
            insertLetter('O', m)
            if isWinner(board, 'O'):
                print('Sorry, O\'s won this time! .....1111111')
                # run = False
            elif isWinner(board, 'X'):
                print('X\'s won this time! Good Job! ....3333333')
                # run = False
        else:
            print('Tie Game! ....88888')
            # run = False
        clickLoop = 1

    redrawGameWindow()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
