import pygame
import random

# === CONSTANTS === (UPPER_CASE names)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# click_loop = 0
screenWidth = 540
screenHeight = 540
gs = 0
b = [' ' for x in range(10)]
win = pygame.display.set_mode((screenWidth, screenHeight))


# === CLASSES === (CamelCase names)


class Tiles(object):
    x = pygame.image.load('images/x_orange.png')
    o = pygame.image.load('images/o_blue.png')
    grid = pygame.image.load('images/bg_box.png')

    def __init__(self, colour, rect, clicked=False):
        self.colour = colour
        self.rect = rect
        self.clicked = clicked

    def draw_grid(self):
        win.blit(self.grid, self.rect)

    def draw_x(self):
        win.blit(self.x, self.rect)
        self.clicked = True

    def draw_o(self):
        win.blit(self.o, self.rect)
        self.clicked = True


# class Button(object):
class Button:

    def __init__(self, text, game_state, x, y):

        self.text = text
        self.game_state = game_state
        self.width = 100
        self.height = 50
        self.gs = self.game_state

        self.image_normal = pygame.Surface((self.width, self.height))
        self.image_normal.fill(BLUE)

        self.image_hovered = pygame.Surface((self.width, self.height))
        self.image_hovered.fill(GREEN)

        self.image = self.image_normal
        self.rect = self.image.get_rect()

        font = pygame.font.Font('freesansbold.ttf', 15)
        # font = pygame.font.SysFont('comicsans', 30, True)

        text_image = font.render(text, True, WHITE)
        text_rect = text_image.get_rect(center=self.rect.center)

        self.image_normal.blit(text_image, text_rect)
        self.image_hovered.blit(text_image, text_rect)

        # you can't use it before `blit`
        self.rect.topleft = (x, y)

        self.hovered = False
        # self.clicked = False

    def update(self):

        if self.hovered:
            self.image = self.image_hovered
        else:
            self.image = self.image_normal

    def draw(self, surface):

        surface.blit(self.image, self.rect)

    def handle_event(self, event):

        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered:
                if self.game_state == 1:
                    print('Playing 2 player mode')
                    T1.draw_grid()
                    T2.draw_grid()
                    T3.draw_grid()
                    T4.draw_grid()
                    T5.draw_grid()
                    T6.draw_grid()
                    T7.draw_grid()
                    T8.draw_grid()
                    T9.draw_grid()
                    gs = self.gs
                elif self.game_state == 2:
                    print('Playing Computer mode')
                    gs = self.gs
                else:
                    print('Button error')
                    gs = 0


# === FUNCTIONS === (lower_case names)

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


# === MAIN === (lower_case names)

T1 = Tiles((0, 0, 0), (0, 0, 180, 180))
T2 = Tiles((0, 0, 0), (0, 180, 180, 180))
T3 = Tiles((0, 0, 0), (0, 360, 180, 180))
T4 = Tiles((0, 0, 0), (180, 0, 180, 180))
T5 = Tiles((0, 0, 0), (180, 180, 180, 180))
T6 = Tiles((0, 0, 0), (180, 360, 180, 180))
T7 = Tiles((0, 0, 0), (360, 0, 180, 180))
T8 = Tiles((0, 0, 0), (360, 180, 180, 180))
T9 = Tiles((0, 0, 0), (360, 360, 180, 180))


def main():
    # --- init ---

    pygame.init()

    pygame.display.set_caption("TicTacToe with Machine Learning by BSpinks")
    run = True
    gs = 0
    click_loop = 0
    clock = pygame.time.Clock()
    win.fill(WHITE)

    # screen_rect = screen.get_rect()

    btn1 = Button('2 Player', 1, 100, 150)
    btn2 = Button('Vs Computer', 2, 250, 150)

    # --- mainloop ---

    while run:

        if click_loop > 0:
            click_loop += 1
        if click_loop > 8:
            click_loop = 0

        # --- events ---

        for event in pygame.event.get():

            # --- global events ---

            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            # elif pygame.mouse.get_pressed()[0] and click_loop == 0:
            #     playMove()
            #     if b.count(' ') > 1:
            #         m = compMove()
            #         b[m] = 'O'
            #         if isWinner(b, 'O'):
            #             print('Sorry, O\'s won this time!')
            #         elif isWinner(b, 'X'):
            #             print('X\'s won this time! Good Job!')
            #     else:
            #         print('Tie Game!')

            # --- objects events ---

            btn1.handle_event(event)
            btn2.handle_event(event)

        # --- updates ---

        btn1.update()
        btn2.update()

        # --- draws ---

        if gs == 0:
            # win.fill(BLACK)
            btn1.draw(win)
            btn2.draw(win)

        pygame.display.update()

        # --- FPS ---

        clock.tick(25)
        click_loop += 1

    # --- the end ---

    pygame.quit()


# ----------------------------------------------------------------------

if __name__ == '__main__':
    main()
