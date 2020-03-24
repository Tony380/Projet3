"""This is our player class"""
import pygame


class Player:
    def __init__(self, position):
        """dictionary to save our moves in order to let pressed the keyboard's key to move"""
        self.pressed = {}
        """this will save the picked up items"""
        self.objects = {}
        self.image = pygame.image.load("ressource/macgyver.png")
        """rect will keep player's coordinates"""
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

    """ method for the player to move in the maze"""
    def move(self, direction):
        if direction == "up":
            self.rect.y -= 40
        elif direction == "down":
            self.rect.y += 40
        elif direction == "right":
            self.rect.x += 40
        elif direction == "left":
            self.rect.x -= 40
