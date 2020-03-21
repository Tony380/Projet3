import pygame
from random import randrange

coord_list_s = []
coord_list_x = []
wall = pygame.image.load("ressource/wall.png")
floor = pygame.image.load("ressource/floor.png")

play = pygame.image.load("ressource/play.jpg")
win = pygame.image.load("ressource/win.jpg")
lose = pygame.image.load("ressource/lose.jpg")


class Game:

    def __init__(self):
        self.player = Player()
        self.ether = Ether()
        self.tube = Tube()
        self.sting = Sting()
        self.syringe = Syringe()
        self.warden = Warden()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
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
