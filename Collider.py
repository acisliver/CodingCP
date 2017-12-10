#모든 충돌
import pygame
from Healbar import Healbar

class Collider:
    badguys=[]
    collplayer=[]
    heallgauge=194
    heal=None

    def __init__(self,screen,badguys,player2):
        self.screen=screen
        self.badguys=badguys
        self.collplayer=player2

    def collide(self):
        self.heal = Healbar(self.screen, self.heallgauge)

        for badguy in self.badguys:
            if self.collplayer.colliderect(badguy):
                self.badguys.remove(badguy)
                self.heallgauge -= 200
                self.heal = Healbar(self.screen, self.heallgauge)
        self.heal.drow()