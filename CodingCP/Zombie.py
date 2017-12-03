import pygame

class Zombie(pygame.Rect):
    zombie1 = pygame.image.load("resources/images/zombie1.png")
    zombie2 = pygame.image.load("resources/images/zombie2.png")
    zom_lst = [zombie1, zombie2]
    screen = None
    def __init__(self, screen, x ,y, zom_num):
        super().__init__(self.zombie1.get_rect(center=(x,y)))
        self.screen = screen
        self.top = x
        self.left = y
        self.zom_num = zom_num

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            if (50 < self.left):
                self.left -= 15
        if pressed[pygame.K_DOWN]:
            if (self.left < 800):
                self.left += 15

        if pressed[pygame.K_RIGHT]:
            if (self.top < 600):
                self.top += 15
        if pressed[pygame.K_LEFT]:
            if (0 < self.top):
                self.top -= 15

        self.screen.blit(self.zom_lst[self.zom_num], (self.top, self.left))

