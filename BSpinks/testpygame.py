import pygame

pygame.init()

screenWidth = 1000
screenHeight = 640

win = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('R1.png'),
             pygame.image.load('R2.png'),
             pygame.image.load('R3.png'),
             pygame.image.load('R4.png'),
             pygame.image.load('R5.png'),
             pygame.image.load('R6.png'),
             pygame.image.load('R7.png'),
             pygame.image.load('R8.png'),
             pygame.image.load('R9.png')
             ]
walkLeft = [pygame.image.load('L1.png'),
            pygame.image.load('L2.png'),
            pygame.image.load('L3.png'),
            pygame.image.load('L4.png'),
            pygame.image.load('L5.png'),
            pygame.image.load('L6.png'),
            pygame.image.load('L7.png'),
            pygame.image.load('L8.png'),
            pygame.image.load('L9.png')
            ]
bg = pygame.image.load('beach_bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True

    def draw(self):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                man.walkCount += 1
            elif man.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                man.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))


class Projectile(object):
    def __init__(self, x, y, radius, colour, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.colour, (self.x, self.y), self.radius)


class enemy(object):
    walkRight = [pygame.image.load('R1E.png'),
                 pygame.image.load('R2E.png'),
                 pygame.image.load('R3E.png'),
                 pygame.image.load('R4E.png'),
                 pygame.image.load('R5E.png'),
                 pygame.image.load('R6E.png'),
                 pygame.image.load('R7E.png'),
                 pygame.image.load('R8E.png'),
                 pygame.image.load('R9E.png'),
                 pygame.image.load('R10E.png'),
                 pygame.image.load('R11E.png')
                 ]
    walkLeft = [pygame.image.load('L1E.png'),
                pygame.image.load('L2E.png'),
                pygame.image.load('L3E.png'),
                pygame.image.load('L4E.png'),
                pygame.image.load('L5E.png'),
                pygame.image.load('L6E.png'),
                pygame.image.load('L7E.png'),
                pygame.image.load('L8E.png'),
                pygame.image.load('L9E.png'),
                pygame.image.load('L10E.png'),
                pygame.image.load('L11E.png')
                ]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.walkCount = 0
        self.vel = 3


def redrawGameWindow():
    win.blit(bg, (0, 0))
    man.draw()
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


# MAIN LOOP
man = Player(800, 540, 64, 64)
bullets = []
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if screenWidth > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 50:
            bullets.append(
                Projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 2, (255, 255, 255), facing))

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < screenWidth - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not man.isJump:
        if keys[pygame.K_UP]:
            man.isJump = True
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.25 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()
