import pygame


class Player:
    def __init__(self, position):
        super().__init__()
        self.pressed = {}
        self.objects = {}
        self.image = pygame.image.load("ressource/macgyver.png")
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

    def move(self, direction):
        if direction == "up":
            self.rect.y -= 40
        elif direction == "down":
            self.rect.y += 40
        elif direction == "right":
            self.rect.x += 40
        elif direction == "left":
            self.rect.x -= 40
