#플레이어
import pygame

class Player(pygame.Rect):
    screen=None
    player = pygame.image.load('resources/images/player.png')

    def __init__(self, screen, x, y):
        super().__init__(self.player.get_rect())    #상위 클래스의 함수(rect)를 사용하기 위해 super()사용
        self.screen=screen
        self.top = x
        self.left =y

    def move(self):

        self.top, self.left = pygame.mouse.get_pos()

        self.screen.blit(self.player, (self.top-53, self.left-50))
