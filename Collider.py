#모든 충돌
import pygame
from Healbar import Healbar

class Collider:
    arrows=[]
    badguys=[]
    collplayer=[]
    heallgauge=194
    heal=None

    def __init__(self,sceen,badguys,player):
        self.screen=sceen
        self.badguys=badguys
        self.collplayer=player

    def collide(self):
        self.heal = Healbar(self.screen, self.heallgauge)

        for badguy in self.badguys:
            if self.collplayer.colliderect(badguy):
                self.badguys.remove(badguy)
                self.heallgauge -= 10
                self.heal = Healbar(self.screen, self.heallgauge)
        self.heal.drow()