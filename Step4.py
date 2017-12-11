#함정을 피해서 탈출
import pygame
from Player2 import Player2
from Trap import Trap
from Screen2 import Screen2
from WL import WL
from Arrow import Arrow

class Step4:
    width=1200
    height = 800

    x=100
    y=100
    step4_finisher = True

    background = pygame.image.load('resources/images/grass.png')

    player=[]
    trap = None
    traps = []

    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.player2 = Player2(self.screen ,self.x,self.y)
        self.wl=WL(self.screen)
        self.screen2=Screen2(self.screen,self.width,self.height)

    def Active(self,x,y):
        self.trap = Trap(self.screen, x, y)
        self.trap.draw()
        self.traps.append(self.trap)
        if self.player2.colliderect(self.trap):
            self.wl.print()

    def Step4(self):

        while self.step4_finisher:
            for event in pygame.event.get():    #종료 이벤트
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            pygame.display.update() #업데이트

            for i in range(int(self.width // 100) + 1):     #배경 채우기
                for j in range(int(self.height // 100) + 1):
                    self.screen.blit(self.background, (i * 100, j * 100))
            self.screen.fill((128, 128, 128))

            self.Active(200, 500)
            self.Active(500, 50)
            self.Active(900, 100)
            self.arrow = Arrow(self.screen, 100, 100)
            self.arrow.draw()

            self.player2.move()

            if self.player2.colliderect(self.arrow):
                self.step4_finisher = False
