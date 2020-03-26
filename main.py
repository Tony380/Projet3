"""Main program importing pygame and all our classes"""
import pygame
from maze import Maze
from player import Player
from items import Items


def main():
    pygame.init()
    pygame.display.set_caption("MacGyver's Maze")

    cell_size = 40

    maze = Maze("structure", cell_size)

    height = maze.maze_height * cell_size
    width = maze.maze_width * cell_size

    screen = pygame.display.set_mode((width, height))

    maze.maze(screen)

    player = Player(maze.coord_list_d[0], cell_size)

    guard = Items("guard", pygame.image.load("ressource/guard.png"), cell_size)
    guard.place(screen, maze.coord_list_a)

    ether = Items("ether", pygame.image.load("ressource/ether.png"), cell_size)
    ether.image.set_colorkey((0, 0, 0))

    pipe = Items("pipe", pygame.image.load("ressource/pipe.png"), cell_size)
    pipe.image.set_colorkey((0, 0, 0))

    needle = Items("needle", pygame.image.load("ressource/needle.png"), cell_size)

    ether.place(screen, maze.coord_list_o)
    pipe.place(screen, maze.coord_list_o)
    needle.place(screen, maze.coord_list_o)

    run = True
    while run:
        if player.rect != guard.rect:
            pygame.time.Clock().tick(10)
            screen.blit(maze.floor, player.rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    player.pressed[event.key] = True
                elif event.type == pygame.KEYUP:
                    player.pressed[event.key] = False

            """Player move"""
            if player.pressed.get(pygame.K_UP) and (player.rect.x, player.rect.y - cell_size) \
                    not in maze.coord_list_x and player.rect.y - cell_size >= 0:
                player.move("up")
            elif player.pressed.get(pygame.K_DOWN) and (player.rect.x, player.rect.y + cell_size) \
                    not in maze.coord_list_x and player.rect.y + cell_size < height:
                player.move("down")
            elif player.pressed.get(pygame.K_RIGHT) and (player.rect.x + cell_size, player.rect.y) \
                    not in maze.coord_list_x and player.rect.x + cell_size < width:
                player.move("right")
            elif player.pressed.get(pygame.K_LEFT) and (player.rect.x - cell_size, player.rect.y) \
                    not in maze.coord_list_x and player.rect.x - cell_size >= 0:
                player.move("left")

            """Collecting items"""
            if player.rect.colliderect(ether.rect):
                player.objects["ether"] = ether
            elif player.rect.colliderect(pipe.rect):
                player.objects["pipe"] = pipe
            elif player.rect.colliderect(needle.rect):
                player.objects["needle"] = needle

            screen.blit(player.image, player.rect)

            """Two possible endings"""
            if player.rect.colliderect(guard.rect):
                if len(player.objects) == 3:
                    win = pygame.image.load("ressource/win.jpg")
                    win = pygame.transform.scale(win, (width, height))
                    screen.blit(win, (0, 0))
                else:
                    lose = pygame.image.load("ressource/lose.jpg")
                    lose = pygame.transform.scale(lose, (width, height))
                    screen.blit(lose, (0, 0))
                run = False

            pygame.display.flip()


if __name__ == "__main__":
    main()
