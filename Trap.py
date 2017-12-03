#함정
import pygame

class Trap:
    screen = None
    trap = pygame.image.load("resources/images/trap")
    trap_active = pygame.image.load("resources/images/trap_active")

    def __init__(self, screen, x ,y):
        self.screen = screen
        self.top = x
        self.left = y

    def draw(self):
        self.screen.blit(self.trap, (self.top, self.left))