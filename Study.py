import pygame

class Study:


    screen = None
    player = None
    desks = []
    flag = True
    invincibility_flag = False

    def __init__(self, screen, player, desks, invincibility_flag):
        self.screen = screen
        self.player = player
        self.desks = desks
        self.invincibility_flag = invincibility_flag

    def study(self, desk):
        if self.flag ==True:
            if self.player.colliderect(desk):
                self.invincibility_flag = True
                self.flag = False
            else:
                self.invincibility_flag = False
            print(self.invincibility_flag)
