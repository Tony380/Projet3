import pygame
from maze import Maze
from player import Player


pygame.init()

pygame.display.set_caption("Mac Gyver's Maze")
screen = pygame.display.set_mode((600, 600))

maze = Maze("structure")
maze.maze(screen)

player = Player(maze.coord_list_d[0])

run = True
while run:
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

    screen.blit(player.image, player.rect)


    pygame.display.flip()
