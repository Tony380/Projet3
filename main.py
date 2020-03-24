"""This is our main program.
importing all the files containg our classes"""

import pygame
from maze import Maze
from player import Player
from items import Items

"""initiates our pygame screen"""
pygame.init()

pygame.display.set_caption("Mac Gyver's Maze")
screen = pygame.display.set_mode((600, 600))


def main():
    """we load our maze and the images out of the loop"""
    maze = Maze("structure")
    maze.maze(screen)

    player = Player(maze.coord_list_d[0])

    guard = Items("guard", pygame.image.load("ressource/guard.png"))
    guard.place(screen, maze.coord_list_a)

    ether = Items("ether", pygame.image.load("ressource/ether.png").convert())
    ether.image.set_colorkey((0, 0, 0))
    pipe = Items("pipe", pygame.image.load("ressource/pipe.png").convert())
    pipe.image.set_colorkey((0, 0, 0))
    needle = Items("needle", pygame.image.load("ressource/needle.png"))

    ether.place(screen, maze.coord_list_o)
    pipe.place(screen, maze.coord_list_o)
    needle.place(screen, maze.coord_list_o)

    """below, the main loop of the game"""
    run = True
    while run:
        if player.rect != guard.rect:
            """slowing down to 10 fps for the game not to be so fast"""
            pygame.time.Clock().tick(10)
            screen.blit(maze.floor, player.rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    player.pressed[event.key] = True
                elif event.type == pygame.KEYUP:
                    player.pressed[event.key] = False

            if player.pressed.get(pygame.K_UP) and (player.rect.x, player.rect.y - 40) \
                    not in maze.coord_list_x and player.rect.y - 40 >= 0:
                player.move("up")
            elif player.pressed.get(pygame.K_DOWN) and (player.rect.x, player.rect.y + 40) \
                    not in maze.coord_list_x and player.rect.y + 40 < 600:
                player.move("down")
            elif player.pressed.get(pygame.K_RIGHT) and (player.rect.x + 40, player.rect.y) \
                    not in maze.coord_list_x:
                player.move("right")
            elif player.pressed.get(pygame.K_LEFT) and (player.rect.x - 40, player.rect.y) \
                    not in maze.coord_list_x:
                player.move("left")

            """creating an object counter"""
            if player.rect.colliderect(ether.rect):
                player.objects["ether"] = ether
            elif player.rect.colliderect(pipe.rect):
                player.objects["pipe"] = ether
            elif player.rect.colliderect(needle.rect):
                player.objects["needle"] = ether

            screen.blit(player.image, player.rect)

            """ 2 possibles endings : win or lose"""
            if player.rect.colliderect(guard.rect) and len(player.objects) == 3:
                win = pygame.image.load("ressource/win.jpg")
                screen.blit(win, (0, 0))
                run = False
            elif player.rect.colliderect(guard.rect) and len(player.objects) != 3:
                lose = pygame.image.load("ressource/lose.jpg")
                screen.blit(lose, (0, 0))
                run = False

            """refreshing our screen"""
            pygame.display.flip()


if __name__ == "__main__":
    main()
