"""Items class will build the 3 items of the game and the guard"""
import random
import pygame


class Item:
    """Items and guard attributes"""
    def __init__(self, name, image, cell_size):
        self.name = name
        self.cell_size = cell_size
        self.image = pygame.transform.scale(image, (cell_size, cell_size))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def place(self, screen, list_coord):
        """Place items randomly in the maze avoiding items to have the same spot"""
        position = random.choice(list_coord)
        screen.blit(self.image, position)
        list_coord.remove(position)
        self.rect.x = position[0]
        self.rect.y = position[1]
