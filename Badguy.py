import pygame
import random

class Badguy(pygame.Rect):
    speed=0
    screen = None
    badguy1 = pygame.image.load("resources/images/F.png")
    badguy2 = pygame.image.load("resources/images/practice.png")

    badguys = [badguy1, badguy2]


    def __init__(self, screen, x, y, speed):
        super().__init__(self.badguy1.get_rect())     #상위 클래스의 함수(rect)를 사용하기 위해 super()사용
        super().__init__(self.badguy2.get_rect())
        self.top = x
        self.left = y
        self.speed = speed
        self.screen = screen

    def move(self):             #몹 움직임 함수
        self.left += self.speed
        self.screen.blit(self.badguy2,(self.top,self.left))

    def move2(self):
        self.left += self.speed
        self.screen.blit(self.badguy1, (self.top, self.left))