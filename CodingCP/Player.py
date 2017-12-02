import pygame

class Player(pygame.Rect):
    screen = None
    player = pygame.image.load('resources/images/player.png')
    player_lst=[]
    for x in range(6):
        player_lst.append((x *126, 126, 100, 100))

    def __init__(self, screen, player, x ,y):
        super().__init__(self.player.get_rect(center=(x,y)))
        self.screen = screen
        self.player = player
        self.top = x
        self.left = y

    def update(self):
        self.player_img = pygame.transform.rotate(self.player, 0)
        self.rect = self.player.get_rect()
        self.rect.center = (self.top, self.left)


    def move(self):
        self.screen.blit(self.player, (500, 500), self.player_lst[0])
        self.screen.blit(self.player, (500, 600), self.player_lst[1])
        self.screen.blit(self.player, (500, 700), self.player_lst[2])
        self.screen.blit(self.player, (500, 800), self.player_lst[3])
        self.screen.blit(self.player, (500, 900), self.player_lst[4])
        self.screen.blit(self.player, (500, 1000), self.player_lst[5])

