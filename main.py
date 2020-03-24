import pygame
from maze import Maze
from player import Player
from items import Items


pygame.init()

pygame.display.set_caption("Mac Gyver's Maze")
screen = pygame.display.set_mode((600, 600))


def main():
    maze = Maze("structure")
    maze.maze(screen)

    player = Player(maze.coord_list_d[0])

    guard = Items("guard", pygame.image.load("ressource/guard.png"))
    guard.place(screen, maze.coord_list_a)

    ether = Items("ether", pygame.image.load("ressource/ether.png"))
    pipe = Items("pipe", pygame.image.load("ressource/pipe.png"))
    needle = Items("needle", pygame.image.load("ressource/needle.png"))

    ether.place(screen, maze.coord_list_o)
    pipe.place(screen, maze.coord_list_o)
    needle.place(screen, maze.coord_list_o)

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

        if player.rect.colliderect(ether.rect):
            player.objects["ether"] = ether
        elif player.rect.colliderect(pipe.rect):
            player.objects["pipe"] = ether
        elif player.rect.colliderect(needle.rect):
            player.objects["needle"] = ether

        if player.rect.colliderect(guard.rect) and len(player.objects) == 3:
            print("win")
        elif player.rect.colliderect(guard.rect) and len(player.objects) != 3:
            print("lose")

        screen.blit(player.image, player.rect)

        pygame.display.flip()


if __name__ == "__main__":
    main()
