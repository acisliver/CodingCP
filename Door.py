import pygame

class Door(pygame.Rect):

    screen = None
    door = pygame.image.load("resources/images/door.png")

    def __init__(self, screen, x , y):
        super().__init__(self.door.get_rect())
        self.screen = screen
        self.top = x
        self.left = y

    def draw(self):
        self.screen.blit(self.door, (self.top, self.left))