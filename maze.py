import pygame


class Maze:
    def __init__(self, name):
        self.name = name
        self.structure = self.load_structure()
        self.wall = pygame.image.load("ressource/wall.png")
        self.floor = pygame.image.load("ressource/floor.png")
        self.coord_list_o = []
        self.coord_list_x = []
        self.coord_list_d = []
        self.coord_list_a = []

    def load_structure(self):
        with open(self.name + ".txt") as file:
            grid = file.readlines()
        return grid

    def maze(self, screen):
        coord_y = 0
        for lines in self.structure:
            coord_x = 0
            for letter in lines:
                if letter == "X":
                    self.coord_list_x.append((coord_x, coord_y))
                    screen.blit(self.wall, (coord_x, coord_y))
                    coord_x += 40
                elif letter == "O":
                    self.coord_list_o.append((coord_x, coord_y))
                    screen.blit(self.floor, (coord_x, coord_y))
                    coord_x += 40
                elif letter == "D":
                    self.coord_list_d.append((coord_x, coord_y))
                    screen.blit(self.floor, (coord_x, coord_y))
                    coord_x += 40
                elif letter == "A":
                    self.coord_list_a.append((coord_x, coord_y))
                    screen.blit(self.floor, (coord_x, coord_y))
                    coord_x += 40
            coord_y += 40

