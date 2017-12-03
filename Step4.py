#함정을 피해서 탈출
import pygame
from Player import Player
#from Trap import Trap
from WL import WL
from Screen2 import Screen2

class Screen:
    width=1200
    height = 800

    x=100
    y=100
    exitcode = 0

    background = pygame.image.load('resources/images/grass.png')
    youwin = pygame.image.load("resources/images/youwin.png")

    player=[]
    collider=None
    wl = None
    heallvalue=None


    fpsClock = pygame.time.Clock()
    FPS = 100

    screen = pygame.display.set_mode((width, height))       #화면 해상도
    bg_columns = background.get_width()                     #화면 너비 불러오기
    bg_rows = background.get_height()                       #화면 높이 불러오기

    def __init__(self):
        self.player = Player(self.screen ,self.x,self.y)
        self.wl=WL(self.screen,self.exitcode)
        self.screen2=Screen2(self.screen,self.width,self.height)

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

            self.player.move()      #플레이어 무브함수


            pygame.display.update()

            if self.healgauge < 0:
                break
        if self.healgauge < 0:  #체력게이지가 0보다 작으면
            self.wl.print()     #win or lose 출력

    def Starting(self):
        while True:
            self.screen2.Start()    #스크린2 실행
            game = Screen()
            game.Start()            #스크린1 실행


game2 = Screen()
game2.Starting()