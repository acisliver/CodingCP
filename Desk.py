import pygame

class Desk(pygame.Rect):

    screen = None
    desk = pygame.image.load("resources/images/desk.png")

    def __init__(self, screen, x , y):
        super().__init__(self.desk.get_rect())
        self.screen = screen
        self.top = x
        self.left = y

    def draw(self):
        self.screen.blit(self.desk, (self.top, self.left))