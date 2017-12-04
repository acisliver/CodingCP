#복도에서 좀비 피해서 탈출
import pygame
import random
from Player import Player
from Zombie import Zombie
from Collider import Collider
from WL import WL
from Screen2 import Screen2

class Step2:
    width=1200
    height = 800
    zom_timer = 6
    zombies=[]
    badguy=None
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
        self.collider=Collider(self.screen,self.zombies,self.player)
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
            self.collider.collide() #충돌 함수
            self.healgauge = self.collider.heallgauge

            pygame.display.update()

            for zombie in self.zombies: #몹의 객체만큼
                zombie.move()   #몹 이동 함수
            pygame.display.update()

            self.zom_timer -= 1
            if self.zom_timer == 0:
                zombie = Zombie(self.screen, 0, random.randint(50, self.height - 100), 16)    #위치랜덤의 속도8인 몹 객체 생성
                self.zombies.append(zombie)                                 #리스트에 추가
                self.zom_timer = 15

            if self.healgauge < 0:
                break
        if self.healgauge < 0:  #체력게이지가 0보다 작으면
            self.wl.print()     #win or lose 출력

    def Starting(self):
        while True:
            self.screen2.Start()    #스크린2 실행
            game = Step2()
            game.Start()            #스크린1 실행


game2 = Step2()
game2.Starting()