import pygame
from Zombie import Zombie

pygame.init()
width = 1200
height = 800
background = pygame.image.load('resources/images/grass.png')
player = pygame.image.load('resources/images/player.png')
zombie1 = pygame.image.load("resources/images/zombie1.png")
zombie2 = pygame.image.load("resources/images/zombie2.png")

fpsClock = pygame.time.Clock()
FPS = 100

bg_columns = background.get_width()
bg_rows = background.get_height()

screen = pygame.display.set_mode((width, height))

def Start():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        pygame.display.update()

        for i in range(int(width // bg_columns) + 1):     #배경 채우기
            for j in range(int(height // bg_rows) + 1):
                screen.blit(background, (i * bg_columns, j * bg_rows))
        screen.blit(player, (100, 100))
        screen.blit(zombie1, (200, 200))
        screen.blit(zombie2, (200, 300))

        position = pygame.mouse.get_pos()



Start()


