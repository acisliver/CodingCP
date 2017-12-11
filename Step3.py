#3단계 위에서 내려오는 장애물 피하기
import pygame
import random
from Player import Player
from Badguy import FCredit
from Collider import Collider
from WL import WL
from Arrow2 import  Arrow2

class Step3:
    width=1200
    height = 800
    badtimer = 30
    badguys=[]

    x=100
    y=100
    step3_finisher = True

    background = pygame.image.load('resources/images/grass.png')

    player=[]
    collider=None
    heallvalue=None

    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.player = Player(self.screen ,self.x,self.y)
        self.collider=Collider(self.screen,self.badguys,self.player)
        self.wl=WL(self.screen)

    def Step3(self):

        while self.step3_finisher:
            for event in pygame.event.get():    #종료 이벤트
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            pygame.display.update() #업데이트

            for i in range(int(self.width // 100) + 1):     #배경 채우기
                for j in range(int(self.height // 100) + 1):
                    self.screen.blit(self.background, (i * 100, j * 100))

            self.arrow2 = Arrow2(self.screen, 1000, 650)
            self.arrow2.draw()

            self.player.move()      #플레이어 무브함수
            self.collider.collide() #충돌 함수
            self.healgauge = self.collider.heallgauge
            pygame.display.update()

            for f in self.badguys: #몹의 객체만큼
                f.move()   #몹 이동 함수
            pygame.display.update()

            self.badtimer -= 1
            if self.badtimer == 0:
                f = FCredit(self.screen, random.randint(50, self.width - 50), 0, 10)    #위치랜덤의 속도8인 몹 객체 생성
                self.badguys.append(f)                                 #리스트에 추가
                self.badtimer = 30
            pygame.display.update()
            if self.healgauge < 0:
                break
            if self.player.colliderect(self.arrow2):
                self.step3_finisher = False
        if self.healgauge < 0:  #체력게이지가 0보다 작으면
            self.wl.print()
