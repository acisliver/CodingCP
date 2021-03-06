import pygame
from Player import  Player
from Zombie import Zombie

class Screen:
    width = 1200
    height = 800
    background = pygame.image.load('resources/images/grass.png')
    player = pygame.image.load('resources/images/player.png')
    zombie1 = pygame.image.load("resources/images/zombie1.png")
    zombie2 = pygame.image.load("resources/images/zombie2.png")
    zom_num = 0
    step1 = []
    step2 = []
    step3 = []
    step4 = []

    sprt_clock = 60

    fpsClock = pygame.time.Clock()
    FPS = 100

    bg_columns = background.get_width()
    bg_rows = background.get_height()

    screen = pygame.display.set_mode((width, height))

    player_lst = []
    for x in range(6):
        player_lst.append((x * 126, 126, 100, 100))
    def __init__(self):
        self.player = Player(self.screen, self.player, 100, 100)
        self.zombie = Zombie(self.screen,100, 200, self.zom_num)

    def Start(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            pygame.display.update()

            for i in range(int(self.width // self.bg_columns) + 1):     #배경 채우기
                for j in range(int(self.height // self.bg_rows) + 1):
                    self.screen.blit(self.background, (i * self.bg_columns, j * self.bg_rows))
            #self.screen.blit(self.player, (100, 100))

            if self.sprt_clock >= 60:
                self.zom_num -= 1
                self.zombie.move()
                print(self.zom_num)
                self.sprt_clock-=1
            elif self.sprt_clock <= 0:
                self.zom_num += 1
                self.zombie.move()
                print(self.zom_num)


            position = pygame.mouse.get_pos()



game = Screen()
game.Start()


