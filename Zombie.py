import pygame

class Zombie(pygame.Rect):
    speed=0
    screen = None
    zombie1 = pygame.image.load("resources/images/zombie1.png")
    zombie2 = pygame.image.load("resources/images/zombie2.png")

    def __init__(self, screen, x, y, speed):
        super().__init__(self.zombie1.get_rect())     #상위 클래스의 함수(rect)를 사용하기 위해 super()사용
        self.top = x
        self.left = y
        self.speed = speed
        self.screen = screen

    def move(self):             #몹 움직임 함수
        self.left += self.speed
        self.screen.blit(self.zombie1,(self.top,self.left))