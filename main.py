import pygame
import random

# initialize pygame
pygame.init()

# create a screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Gay Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('ship.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('enemy ufo.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.2
enemyY_change = 40


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Game Loop
running = True
while running:

    # RGB - Red, Green, Blue
    screen.fill((10, 0, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if a key stroke is pressed check which direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.type == pygame.K_SPACE:
                return
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0



    playerX += playerX_change

    if playerX <=0:
        playerX = 0
    elif playerX >=736:
        playerX = 736

    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.2
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.2
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()








