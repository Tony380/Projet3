"""This file contains some variables and all the classes and their respective methods"""

import pygame
from random import randrange

# lists of coordinates to build the maze
coord_list_s = []
coord_list_x = []

wall = pygame.image.load("ressource/wall.png")
floor = pygame.image.load("ressource/floor.png")


# this class contains all other classes in order to charge them at once
class Game:

    def __init__(self):
        self.player = Player()
        self.ether = Ether()
        self.tube = Tube()
        self.sting = Sting()
        self.syringe = Syringe()
        self.warden = Warden()
        self.play = pygame.image.load("ressource/play.jpg").convert()
        self.win = pygame.image.load("ressource/win.jpg").convert()
        self.lose = pygame.image.load("ressource/lose.jpg").convert()



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.objects = 0
        self.items = "empty"
        self.image = pygame.image.load("ressource/MacGyver.png")
        self.rect = self.image.get_rect()
        self.rect.x = 40
        self.rect.y = 0

    def move(self, direction):
        if direction == "up":
            self.rect.y -= 40
        elif direction == "down":
            self.rect.y += 40
        elif direction == "right":
            self.rect.x += 40
        elif direction == "left":
            self.rect.x -= 40


class Ether(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ressource/ether.png")
        # gives some random coordinates for placing in the maze
        self.pos = coord_list_s[randrange(0, len(coord_list_s))]
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.show = True


class Tube(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ressource/tube_plastique.png").convert()
        self.pos = coord_list_s[randrange(0, len(coord_list_s))]
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.show = True


class Sting(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ressource/aiguille.png")
        self.pos = coord_list_s[randrange(0, len(coord_list_s))]
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.show = True


class Syringe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ressource/seringue.png")
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 480
        self.show = False


class Warden(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ressource/Gardien.png")
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 560
        self.show = True
