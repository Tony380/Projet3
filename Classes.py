"""In this file we keep all our classes and their respective methods"""

import pygame
from random import randrange

# couple of variables containing lists
coord_list_s = []
coord_list_x = []


# this class will generate all other classes in our game at once
class Game:
    def __init__(self):
        self.player = Player()
        self.ether = Ether()
        self.tube = Tube()
        self.sting = Sting()
        self.syringe = Syringe()
        self.warden = Warden()


# this class inherits Sprite class properties and will generate the sprite of MacGyver
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # this attribute will eventually change to "full" in order to make appear syringe item in the maze
        self.items = "empty"
        # will contain the image of MacGyver
        self.image = pygame.image.load("ressource/MacGyver.png")
        # rect represents the sprite's coordinates
        self.rect = self.image.get_rect()
        self.rect.x = 40
        self.rect.y = 0

# a move method allowing MacGyver to move in the maze
    def move(self, direction):
        if direction == "up":
            # will move 40 pixels in up direction
            self.rect.y -= 40
        elif direction == "down":
            self.rect.y += 40
        elif direction == "right":
            self.rect.x += 40
        elif direction == "left":
            self.rect.x -= 40


# ether item
class Ether(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ressource/ether.png")
        # picking in self.pos random coordinates from a list containing free path coordinates
        self.pos = coord_list_s[randrange(0, len(coord_list_s))]
        self.rect = self.image.get_rect()
        # getting x and y coordinates from tuple contained in self.pos
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]


# tube item
class Tube(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ressource/tube_plastique.png")
        self.pos = coord_list_s[randrange(0, len(coord_list_s))]
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]


# sting item
class Sting(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ressource/aiguille.png")
        self.pos = coord_list_s[randrange(0, len(coord_list_s))]
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]


# syringe item
class Syringe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ressource/seringue.png")
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 480


# this class will creat the warden
class Warden(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ressource/Gardien.png")
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 560
