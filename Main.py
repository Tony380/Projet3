""" This is the main file which will run the game
We import pygame for the screen, randrange for random coordinates,
maze_structure from Structure.py to build the maze.
From Classes, Game to load the objects, and the coord lists to place items"""

import pygame
from random import randrange
from Structure import maze_structure
from Classes import Game, coord_list_s, coord_list_x

pygame.init()

pygame.display.set_caption("Mac Gyver's Maze")
screen = pygame.display.set_mode((600, 600))

# this put some music
song = pygame.mixer.Sound("ressource/MacGyverSong.ogg")
song.set_volume(0.02)
song.play(10, 0)

# first loop to create our pygame screen
while True:
    # will turn off the pygame screen if shutting it with the mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    # this function will build the maze
    def maze():
        wall = pygame.image.load("ressource/wall.png")
        floor = pygame.image.load("ressource/floor.png")
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
        coord_list_s.pop(-1)
        coord_list_s.pop(-2)

    maze()

    # iniating all other objects
    game = Game()

    # this will avoid double coordinates
    while game.tube.pos == game.ether.pos:
        game.tube.pos = coord_list_s[randrange(0, len(coord_list_s))]
    while game.sting.pos == game.ether.pos or game.sting.pos == game.tube.pos:
        game.sting.pos = coord_list_s[randrange(0, len(coord_list_s))]

    screen.blit(game.play, (0, 0))

    # opening menu
    menu = ""

    # second loop will contain our menu
    while True:
        # player can't move once game is over
        if not game.player.rect.colliderect(game.warden.rect):
            # indicating the move according to the key pressed
            if game.pressed.get(pygame.K_UP) and (game.player.rect.x, game.player.rect.y - 40)\
                    not in coord_list_x and game.player.rect.y - 40 >= 0:
                game.player.move("up")
            elif game.pressed.get(pygame.K_DOWN) and (game.player.rect.x, game.player.rect.y + 40)\
                    not in coord_list_x and game.player.rect.y + 40 < 600:
                game.player.move("down")
            elif game.pressed.get(pygame.K_RIGHT) and (game.player.rect.x + 40, game.player.rect.y)\
                    not in coord_list_x:
                game.player.move("right")
            elif game.pressed.get(pygame.K_LEFT) and (game.player.rect.x - 40, game.player.rect.y)\
                    not in coord_list_x:
                game.player.move("left")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
                if event.key == pygame.K_p:
                    menu = "p"
                elif event.key == pygame.K_e:
                    menu = "e"
                elif event.key == pygame.K_m:
                    menu = "m"
            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False

        # this option open start the game
        if menu == "p":
            maze()

            screen.blit(game.player.image, game.player.rect)

            # for an object, when show is True, the object will appear on the screen
            if game.ether.show:
                # remove the black color background of our image
                game.ether.image.set_colorkey((0, 0, 0))
                screen.blit(game.ether.image, game.ether.pos)

            if game.tube.show:
                game.tube.image.set_colorkey((0, 0, 0))
                screen.blit(game.tube.image, game.tube.pos)

            if game.sting.show:
                screen.blit(game.sting.image, game.sting.pos)

            if game.syringe.show:
                game.syringe.image.set_colorkey((0, 0, 0))
                screen.blit(game.syringe.image, game.syringe.rect)

            if game.warden.show:
                screen.blit(game.warden.image, game.warden.rect)

            # detection of player picking items
            if game.player.rect.colliderect(game.ether.rect):
                game.ether.show = False
                game.player.objects[game.ether] = "Ether"
            elif game.player.rect.colliderect(game.tube.rect):
                game.player.objects[game.tube] = "Tube"
                game.tube.show = False
            elif game.player.rect.colliderect(game.sting.rect):
                game.player.objects[game.sting] = "Sting"
                game.sting.show = False
            elif game.player.rect.colliderect(game.syringe.rect) and len(game.player.objects) == 3:
                game.syringe.show = False
                game.player.objects[game.syringe] = "Syringe"
                game.player.items = "full"

            if len(game.player.objects) == 3:
                game.syringe.show = True

            # below 2 possible endings when MacGyver and warden are on the same spot => win or lose
            if len(game.player.objects) == 4 and game.player.rect.colliderect(game.warden.rect):
                game.warden.show = False
                screen.blit(game.win, (0, 0))
                menu = ""
            elif len(game.player.objects) < 4 and game.player.rect.colliderect(game.warden.rect):
                screen.blit(game.lose, (0, 0))
                menu = ""

        # to go back to the opening menu
        elif menu == "m":
            break
        # option to quit the game
        elif menu == "e":
            quit()

        # Refreshing the screen for our loop
        pygame.display.flip()
