#복도에서 좀비 피해서 탈출
import pygame
import random
from Player2 import Player2
from Zombie import Zombie
from Collider import Collider
from WL import WL
from Arrow import Arrow

class Step2:

    zom_timer = 20
    zombies=[]
    badguy=None
    x=100
    y=100
    exitcode = 0

    background = pygame.image.load('resources/images/grass.png')
    waydoor = pygame.image.load("resources/images/waydoor.png")

    player=[]
    collider=None
    wl = None
    heallvalue=None

    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.player2 = Player2(self.screen ,self.x,self.y)
        self.collider=Collider(self.screen,self.zombies,self.player2)
        self.wl=WL(self.screen,self.exitcode)

    def Step2(self):
        finisher = True
        while finisher:
            for event in pygame.event.get():    #종료 이벤트
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            pygame.display.update() #업데이트

            for i in range(int(self.width // 100) + 1):     #배경 채우기
                for j in range(int(self.height // 100) + 1):
                    self.screen.blit(self.background, (i * 100, j * 100))
            self.screen.fill((128, 128, 128))

            self.screen.blit(self.waydoor, (100, 100))
            self.screen.blit(self.waydoor, (500, 100))
            self.screen.blit(self.waydoor, (900, 100))

            self.arrow = Arrow(self.screen, 100, 700)
            self.arrow.draw()

            self.player2.move()      #플레이어 무브함수
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
                self.zom_timer = 20


            if self.healgauge < 0:
                break
            if self.player2.colliderect(self.arrow):
                finisher = False

        if self.healgauge < 0:  #체력게이지가 0보다 작으면
            self.wl.print()     #win or lose 출력


