import pygame

class Zombie(pygame.rect):
    zombie1 = pygame.image.load("resources/images/zombie1.png")
    zombie2 = pygame.image.load("resources/images/zombie2.png")
    speed=0
    num=0
    timer=1
    screen = None
    MobNum=0


    def __init__(self, screen, x, y, speed,time,num):
        super().__init__(self.badguyimg.get_rect())
        self.speed = speed
        self.screen = screen
        self.time=time
        self.num=num
        self.width=70
        self.height=70
        self.top = x - self.height/2
        self.left = y - self.width/2

    def move(self):

