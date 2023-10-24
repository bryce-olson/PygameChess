import pygame

pygame.init()
SCREEN_SIZE = 700
SQUARE_SIZE = SCREEN_SIZE / 8
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

font_size = int(SQUARE_SIZE/4)
font = pygame.font.SysFont("Arial", font_size)
darkColor = (118, 150, 56)
lightColor = (238, 238, 210)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def printSquare(mPos):
    rank = 8 - int(mPos[1] / SQUARE_SIZE)
    file = chr(ord('A')+int(mPos[0] / SQUARE_SIZE))
    print(file+str(rank))


def printBoard():
    for x in range(8):
        for y in range(8):
            sColor = lightColor if (x+y) % 2 == 0 else darkColor
            tColor = lightColor if (x+y) % 2 == 1 else darkColor
            pygame.draw.rect(screen, sColor, pygame.Rect(
                x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if x == 0:
                draw_text(str(8-y), font, tColor, 0, y*SQUARE_SIZE)
            if y == 7:
                draw_text(chr(ord('A') + x), font, tColor, (x+1) *
                          SQUARE_SIZE - font_size, (y+1)*SQUARE_SIZE-font_size)


def redSquare(sPos):
    x = int(sPos[0] / SQUARE_SIZE)
    y = int(sPos[1]/SQUARE_SIZE)
    # print("redsquarring " +str(x) + str(y))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(
        x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    pygame.display.flip()


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            printSquare(pygame.mouse.get_pos())
            redSquare(pygame.mouse.get_pos())
    printBoard()
    pygame.display.flip()

print("quitting!")
pygame.quit()
