#교수님 몰래 강의실 탈출
import pygame
from Player import Player

class Step1:
    width = 1200
    height = 800

    x = 275
    y = 240

    face = "front"

    face_timer = 20

    screen = pygame.display.set_mode((width, height))
    desk = pygame.image.load("resources/images/desk.png")
    front = pygame.image.load("resources/images/face.png")
    #back = pygame.image.load("resources/images/back.png")
    #door = pygame.image.load("resources/images/door.png")

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

            #self.screen.blit(self.door, (1100, 750))

            for i  in range(3):
                for j in range(3):
                    self.screen.blit(self.desk, (275 + self.width/5 * i, 240 + self.height/5 *j))

            self.player.move()

            self.face_timer -= 1

            if self.face_timer ==0:
                if self.face == "front":
                    self.screen.blit(self.front, (525, 25))
                    self.face_timer = 20
                    self.face = "back"
                    #if 특정 위치라면:
                        #break
                    #else:
                        #게임오버
                #elif self.face == "back"
                    #self.screen.blit(self.back, (525, 25))
                    #self.face_timer = 20
                    #self.face = "front"

game = Step1()
game.Step1()