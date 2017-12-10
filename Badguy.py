import pygame
import random

class FCredit(pygame.Rect):
    speed=0
    screen = None
    f_Credit = pygame.image.load("resources/images/F.png")

    def __init__(self, screen, x, y, speed):
        super().__init__(self.f_Credit.get_rect())     #상위 클래스의 함수(rect)를 사용하기 위해 super()사용
        self.top = x
        self.left = y
        self.speed = speed
        self.screen = screen

    def move(self):             #몹 움직임 함수
        self.left += self.speed
        self.screen.blit(self.f_Credit,(self.top,self.left))

class  Assignment(pygame.Rect):
    speed=0
    screen = None
    assignment = pygame.image.load("resources/images/practice.png")

    def __init__(self, screen, x, y, speed):
        super().__init__(self.assignment.get_rect())     #상위 클래스의 함수(rect)를 사용하기 위해 super()사용
        self.top = x
        self.left = y
        self.speed = speed
        self.screen = screen

    def move2(self):             #몹 움직임 함수
        self.left += self.speed
        self.screen.blit(self.assignment,(self.top,self.left))
