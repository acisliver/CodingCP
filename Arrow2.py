import pygame

class Arrow2(pygame.Rect):
    speed=0
    screen = None
    arrow2 = pygame.image.load("resources/images/arrow2.png")

    def __init__(self,screen,x,y):
        super().__init__(self.arrow2.get_rect())     #상위 클래스의 함수(rect)를 사용하기 위해 super()사용
        self.top=x
        self.left=y
        self.screen=screen

    def draw(self):
        self.screen.blit(self.arrow2, (self.top, self.left))