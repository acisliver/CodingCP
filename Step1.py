#교수님 몰래 강의실 탈출
import pygame
from Player import Player
from Study import Study
from Desk import Desk

class Step1:
    width = 1200
    height = 800

    x = 275
    y = 240

    face = "back"

    desk = None
    desks = []

    invincibility_flag = False

    face_timer = 700

    screen = pygame.display.set_mode((width, height))

    front = pygame.image.load("resources/images/front.png")
    back = pygame.image.load("resources/images/back.png")
    door = pygame.image.load("resources/images/door.png")
    board = pygame.image.load("resources/images/board.png")

    fpsClock = pygame.time.Clock()
    FPS = 100

    def __init__(self):
        self.player = Player(self.screen, self.x, self.y)
        self.study = Study(self.screen, self.player, self.desks, self.invincibility_flag)


    def Step1(self):

        finisher=True
        while finisher:
            for event in pygame.event.get():    #종료 이벤트
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            pygame.display.update()

            self.screen.fill((135, 135, 135))

            self.screen.blit(self.door, (1000, 600))
            self.screen.blit(self.board, (50, 100))

            for i in range(3):
                for j in range(3):
                    self.desk = Desk(self.screen, 275 + self.width/5 * i, 340 + self.height/5 *j)
                    self.desk.draw()
                    self.desks.append(self.desk)
            self.study.study(self.desk)

            self.player.move()

            if self.face == "front":
                if self.study.invincibility_flag==True:
                    print(2)
                else:
                    print(1)

            if self.face == "front":
                self.screen.blit(self.front, (700, 50))
            elif self.face == "back":
                self.screen.blit(self.back, (700, 50))
            self.face_timer -= 1

            if self.face_timer ==0:
                if self.face == "front":
                    self.face_timer = 700
                    self.face = "back"

                elif self.face == "back":
                    self.face_timer = 300
                    self.face = "front"


game = Step1()
game.Step1()