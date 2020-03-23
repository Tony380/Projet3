"""This file contains some variables and all the classes and their respective methods.
We import pygame here for loading images and inherit from sprite class"""

import pygame
from random import randrange
import time

# lists of coordinates to build the maze and then give son coordinates to items
coord_list_s = []
coord_list_x = []


# this class contains all other classes in order to load them all at once
class Game:
    def __init__(self):
        # below a dictionary keeping the items MacGyver has picked up
        self.pressed = {}
        self.player = Player()
        self.ether = Ether()
        self.tube = Tube()
        self.sting = Sting()
        self.syringe = Syringe()
        self.warden = Warden()
        self.play = pygame.image.load("ressource/play.jpg")
        self.win = pygame.image.load("ressource/win.jpg")
        self.lose = pygame.image.load("ressource/lose.jpg")


# this class represents MacGyver in the game and inherits from Sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # here we create a dictionary to save the items MacGyver picks up
        self.objects = {}
        self.image = pygame.image.load("ressource/MacGyver.png")
        # self.rect indicates 4 figures about our object : <abscissa, ordered, width and height>
        self.rect = self.image.get_rect()
        self.rect.x = 40
        self.rect.y = 0

    # method for player to move in the maze
    def move(self, direction):
        time.sleep(0.1)
        if direction == "up":
            self.rect.y -= 40
        elif direction == "down":
            self.rect.y += 40
        elif direction == "right":
            self.rect.x += 40
        elif direction == "left":
            self.rect.x -= 40


# below classes which represents the items MacGyver has to pick up
class Ether(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ressource/ether.png")
        # gives some random coordinates for placing in the maze
        self.pos = coord_list_s[randrange(0, len(coord_list_s))]
        self.rect = self.image.get_rect()
        # below we stock some coordinates on x and y for abscissa and ordered
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.show = True


class Tube(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ressource/tube_plastique.png")
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
        self.image = pygame.image.load("ressource/seringue.png").convert()
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
