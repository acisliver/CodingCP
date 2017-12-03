#교수님 몰래 강의실 탈출
import pygame
from Player import Player

class Step1:
    width = 1200
    height = 800

    x = 275
    y = 240

    face = "front"

    screen = pygame.display.set_mode((width, height))
    desk = pygame.image.load("resources/images/desk.png")
    faceimg = pygame.image.load("resources/images/face.png")

    fpsClock = pygame.time.Clock()
    FPS = 100

    def __init__(self):
        self.player = Player(self.screen, self.x, self.y)



    def Step1(self):
        finisher=True
        while finisher:
            for event in pygame.event.get():    #종료 이벤트
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            pygame.display.update()

            self.screen.fill((128, 128, 128))

            for i  in range(3):
                for j in range(3):
                    self.screen.blit(self.desk, (275 + self.width/5 * i, 240 + self.height/5 *j))

            self.player.move()

            if self.face == "front":
                self.screen.blit(self.faceimg, (525, 25))






game = Step1()
game.Step1()