import pygame


class Player:
    def __init__(self, position, cell_size):
        super().__init__()
        self.pressed = {}
        self.objects = {}
        self.image = pygame.image.load("ressource/macgyver.png")
        self.image = pygame.transform.scale(self.image, (cell_size, cell_size))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.velocity = cell_size

    def move(self, direction):
        if direction == "up":
            self.rect.y -= self.velocity
        elif direction == "down":
            self.rect.y += self.velocity
        elif direction == "right":
            self.rect.x += self.velocity
        elif direction == "left":
            self.rect.x -= self.velocity
