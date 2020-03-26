"""Class Maze with one method to load a maze from a text file and another method to build it"""
import pygame


class Maze:
    def __init__(self, file_name, cell_size):
        self.name = file_name
        self.cell_size = cell_size
        self.structure = self.load_structure()
        self.maze_height = len(self.structure)
        self.maze_width = len(self.structure[0])
        self.wall = pygame.image.load("ressource/wall.png")
        self.wall = pygame.transform.scale(self.wall, (cell_size, cell_size))
        self.floor = pygame.image.load("ressource/floor.png")
        self.floor = pygame.transform.scale(self.floor, (cell_size, cell_size))
        self.coord_list_o = []
        self.coord_list_x = []
        self.coord_list_d = []
        self.coord_list_a = []

    def load_structure(self):
        with open(self.name + ".txt", "r") as file:
            grid = file.readlines()
            for i in range(len(grid)):
                grid[i] = grid[i].strip()
        return grid

    def maze(self, screen):
        coord_y = 0
        for lines in self.structure:
            coord_x = 0
            for letter in lines:
                if letter == "X":
                    self.coord_list_x.append((coord_x, coord_y))
                    screen.blit(self.wall, (coord_x, coord_y))
                elif letter == "O":
                    self.coord_list_o.append((coord_x, coord_y))
                    screen.blit(self.floor, (coord_x, coord_y))
                elif letter == "D":
                    self.coord_list_d.append((coord_x, coord_y))
                    screen.blit(self.floor, (coord_x, coord_y))
                elif letter == "A":
                    self.coord_list_a.append((coord_x, coord_y))
                    screen.blit(self.floor, (coord_x, coord_y))
                coord_x += self.cell_size
            coord_y += self.cell_size
        self.coord_list_o.pop(-1)
        self.coord_list_o.pop(-2)
