#함정을 피해서 탈출
import pygame
from Player import Player
from Trap import Trap
from WL import WL
from Screen2 import Screen2

class Screen:
    width=1200
    height = 800

    x=100
    y=100
    exitcode = 0

    background = pygame.image.load('resources/images/grass.png')

    player=[]
    trap = None
    traps = []

    fpsClock = pygame.time.Clock()
    FPS = 100

    screen = pygame.display.set_mode((width, height))       #화면 해상도
    bg_columns = background.get_width()                     #화면 너비 불러오기
    bg_rows = background.get_height()                       #화면 높이 불러오기

    def __init__(self):
        self.player = Player(self.screen ,self.x,self.y)
        self.wl=WL(self.screen,self.exitcode)
        self.screen2=Screen2(self.screen,self.width,self.height)


    def Active(self,x,y):
        self.trap = Trap(self.screen, x, y)
        self.trap.draw()
        self.traps.append(self.trap)
        if self.player.colliderect(self.trap):
            print(2)

    def Start(self):
        while True:
            for event in pygame.event.get():    #종료 이벤트
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            pygame.display.update() #업데이트

            for i in range(int(self.width // self.bg_columns) + 1):     #배경 채우기
                for j in range(int(self.height // self.bg_rows) + 1):
                    self.screen.blit(self.background, (i * self.bg_columns, j * self.bg_rows))
            self.screen.fill((128, 128, 128))

            self.Active(200, 500)
            self.Active(500, 100)
            self.Active(900, 100)
            self.Active(1000, 400)
            self.Active(700, 650)

            self.player.move()      #플레이어 무브함수

            pygame.display.update()


game = Screen()
game.Start()