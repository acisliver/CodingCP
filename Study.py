import pygame

class Study:

    screen = None
    player = None
    desks = []
    invincibility_flag = False

    def __init__(self, screen, player, desks, invincibility_flag):
        self.screen = screen
        self.player = player
        self.desks = desks
        self.invincibility_flag = invincibility_flag

    def study(self):
        self.invincibility_flag = False
        for desk in self.desks:
            if self.player.colliderect(desk):
                self.invincibility_flag = True

