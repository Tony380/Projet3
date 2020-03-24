"""this file contains the item class wich will create all our items and the guard"""
import random


class Items:
    def __init__(self, name, image):
        self.name = name
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    """this method will automatically place our items with giving them the same spot"""
    def place(self, screen, list_coord):
        position = random.choice(list_coord)
        screen.blit(self.image, position)
        list_coord.remove(position)
        self.rect.x = position[0]
        self.rect.y = position[1]
