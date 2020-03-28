"""Player class and its method to move in the maze"""
import pygame


class Player:
    """MacGyver's class"""
    def __init__(self, position, cell_size):
        self.pressed = {}
        self.objects = {}
        self.image = pygame.image.load("ressource/macgyver.png")
        self.image = pygame.transform.scale(self.image, (cell_size, cell_size))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.cell_size = cell_size

    def move(self, direction):
        """Move method for player"""
        if direction == "up":
            self.rect.y -= self.cell_size
        elif direction == "down":
            self.rect.y += self.cell_size
        elif direction == "right":
            self.rect.x += self.cell_size
        elif direction == "left":
            self.rect.x -= self.cell_size
