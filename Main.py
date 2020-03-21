""" This is the main file which will run the game"""

import pygame
from random import randrange
from Structure import maze_structure
from Classes import Game, coord_list_s, coord_list_x

pygame.init()

pygame.display.set_caption("Mac Gyver's Maze")
screen = pygame.display.set_mode((600, 600))

wall = pygame.image.load("ressource/wall.png")
floor = pygame.image.load("ressource/floor.png")

song = pygame.mixer.Sound("ressource/MacGyverSong.ogg")
song.set_volume(0.02)
song.play(10, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    # this function will build the maze
    def maze():
        coord_y = 0
        for element in maze_structure:
            coord_x = 0
            for letter in element:
                if letter == "X":
                    coord_list_x.append((coord_x, coord_y))
                    screen.blit(wall, (coord_x, coord_y))
                    coord_x += 40
                elif letter == " ":
                    coord_list_s.append((coord_x, coord_y))
                    screen.blit(floor, (coord_x, coord_y))
                    coord_x += 40
                elif letter == "D":
                    screen.blit(floor, (coord_x, coord_y))
                    coord_x += 40
                elif letter == "A":
                    screen.blit(floor, (coord_x, coord_y))
                    coord_x += 40
            coord_y += 40

    maze()
    coord_list_s.pop(-1)
    coord_list_s.pop(-2)

    game = Game()

    # this will avoid double coordinates
    while game.tube.pos == game.ether.pos:
        game.tube.pos = coord_list_s[randrange(0, len(coord_list_s))]
    while game.sting.pos == game.ether.pos or game.sting.pos == game.tube.pos:
        game.sting.pos = coord_list_s[randrange(0, len(coord_list_s))]

    screen.blit(game.play, (0, 0))
    menu = ""

    # second loop will contain our menu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    menu = "p"
                elif event.key == pygame.K_e:
                    menu = "e"
                elif event.key == pygame.K_m:
                    menu = "m"
                elif event.key == pygame.K_UP and (
                        # player won't get out of the frame
                        game.player.rect.x, game.player.rect.y - 40) not in coord_list_x and \
                        game.player.rect.y - 40 > -40:
                    game.player.move("up")
                elif event.key == pygame.K_DOWN and (
                        game.player.rect.x, game.player.rect.y + 40) not in coord_list_x:
                    game.player.move("down")
                elif event.key == pygame.K_RIGHT and (
                        game.player.rect.x + 40, game.player.rect.y) not in coord_list_x:
                    game.player.move("right")
                elif event.key == pygame.K_LEFT and (
                        game.player.rect.x - 40, game.player.rect.y) not in coord_list_x:
                    game.player.move("left")

        # first menu : game
        if menu == "p":
            maze()

            screen.blit(game.player.image, game.player.rect)

            if game.ether.show:
                game.ether.image.set_colorkey((0, 0, 0))
                screen.blit(game.ether.image, game.ether.pos)

            if game.tube.show:
                game.tube.image.set_colorkey((0, 0, 0))
                screen.blit(game.tube.image, game.tube.pos)

            if game.sting.show:
                screen.blit(game.sting.image, game.sting.pos)

            if game.syringe.show:
                game.syringe.image.set_colorkey((255, 255, 255))
                screen.blit(game.syringe.image, game.syringe.rect)

            if game.warden.show:
                screen.blit(game.warden.image, game.warden.rect)

            # detection of player picking items
            if game.player.rect.colliderect(game.ether.rect):
                game.ether.show = False
            elif game.player.rect.colliderect(game.tube.rect):
                game.tube.show = False
            elif game.player.rect.colliderect(game.sting.rect):
                game.sting.show = False
            elif game.player.rect.colliderect(game.syringe.rect):
                if game.ether.show is False and game.tube.show is False and game.sting.show is False:
                    game.player.items = "full"

            # syringe will appear
            if game.ether.show is False and game.tube.show is False and game.sting.show is False:
                game.syringe.show = True

            if game.ether.show is False and game.tube.show is False and game.sting.show\
                    is False and game.player.items == "full":
                game.syringe.show = False

            # end of game with 2 options, win or lose
            if game.player.items == "full" and game.player.rect.colliderect(game.warden.rect):
                game.warden.show = False
                screen.blit(game.win, (0, 0))
                menu = ""
            elif game.player.items == "empty" and game.player.rect.colliderect(game.warden.rect):
                screen.blit(game.lose, (0, 0))
                menu = ""

        # back to the menu
        elif menu == "m":
            break
        elif menu == "e":
            quit()

        pygame.display.flip()
